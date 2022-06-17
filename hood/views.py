from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import RegisterForm

class SignUpView(View):
    form_class = RegisterForm
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
            
            return redirect(to='/')
        
        return render(request,self.template_name,{'form':form})
            


def index(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')

def viewProfile(request):
    return render(request,'main/view_profile.html')

def comment(request):
    return render(request, 'main/comment.html')
