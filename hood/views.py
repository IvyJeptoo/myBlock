from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from .forms import *
from django.http import HttpResponseRedirect
from .models import *


class SignUpView(View):
    form_class = SignUpForm
    initial = {'key':'value'}
    template_name = 'registration/signup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self, request,*args,**kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, your account has been created successfully!')
            
            return redirect(to='login')
        
        return render(request,self.template_name,{'form':form})
    
class CustomLoginView(LoginView):
    form_class = LoginView
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        
        if not remember_me:
             # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)
            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
         # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView,self).form_valid(form)
    
def viewProfile(request):
    posts = request.user.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        
        
        if profile_form.is_valid() and  user_form.is_valid():             
            user_form.save()         
            profile_form.save()
            return redirect (to='viewProfile')
            # return HttpResponseRedirect(request.path_info)    
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        user_form = UpdateUserForm(instance=request.user)
       
    return render(request,'main/view_profile.html', {'profile_form': profile_form,'user_form': user_form, 'posts':posts})

def createProfile(request):
    current_user = request.user
    if request.method == 'POST':
        create_form = CreateProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if create_form.is_valid() :
            profile = create_form.save(commit=False)
            profile.user = current_user
            profile.save()
            # create_form.save()
            
        return HttpResponseRedirect('home')
    else:
        create_form = CreateProfileForm(instance=request.user.profile)      
             
    return render(request, 'main/hoodform.html', {'create_form':create_form})

def visit(request):
    if request.user.profile.hood == '1':
        return redirect('createProfile')
    
    else:
        return redirect('home')
        
            


def index(request):
    return render(request, 'main/index.html')


def home(request):
    current_user = request.user
    posts = Post.objects.all()
    businesses = Business.objects.all()
    alerts = Alert.objects.all()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            alert_form = AlertForm(request.POST)
            if alert_form.is_valid():
                alert = alert_form.save(commit=False)
                alert.user = current_user
                alert.save()
            return redirect('home')
        elif request.POST.get("form_type") == 'formTwo':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = current_user
                post.save()
                return redirect('home')
            # return redirect(reverse('home') + '#formThree')
        else:
            business_form = BusinessForm(request.POST)
            if business_form.is_valid():
                business = business_form.save(commit=False)
                business.user = request.user
                business.save()
            return redirect('home')
    else:
        alert_form = AlertForm()
        post_form = PostForm()
        business_form = BusinessForm()

    return render(request, 'main/home.html',
                  {'posts': posts, 'alerts': alerts, 'businesses': businesses, 'post_form': post_form,
                   'business_form': business_form, 'alert_form': alert_form})
     
        
    
    

def comment(request, id):
    
    post = get_object_or_404(Post, pk=id)
    comments = post.comment.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user.profile
            comment.save()
            
        return HttpResponseRedirect(request.path_info)
    
    else:
        comment_form = CommentForm()
        
        context = {
            'post': post,
            'comments': comments,
            'comment_form':comment_form,        
            
        }
    return render(request, 'main/comment.html',context)


def searchBusiness(request):
    if 'search-business' in request.GET and request.GET['search-business']:
        name = request.GET.get('search-business')
        results = Business.search_business(name)
        message = name
        context = {
            'results':results,
            'message':message
        }
        return render(request, 'main/results.html', context)
    else:
        message = 'Sorry, such a business does not exist'
    return render(request, 'main/results.html',{'message':message})


def deleteAlert(request, id):
    alert = Alert.objects.get(pk = id)
    alert.delete()
    return HttpResponseRedirect('delete')

    
