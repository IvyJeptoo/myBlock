from email.policy import default
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your models here.
HOODS = (
    ('Kilimani','Kilimani'),
    ('Kileleshwa','Kileleshwa'),
    ('Westlands','Westlands'),
    
)
PRIORITY = (
    ('High Priority','High Priority'),
    ('Low Priority','Low Priority')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = CloudinaryField('image',default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.CharField(max_length=300) 
    hood = models.CharField( max_length=15, choices=HOODS, default=1)

    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            
            
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save()

    def update_profile(self, user, photo, bio):
        self.user = user
        self.photo = photo
        self.bio = bio
        self.save()
    
    
    
    def __str__(self):
        return self.bio
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    detail = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        ordering = ["-pk"]
        
    @classmethod
    def posts(cls):
        posts = cls.objects.all()
        return posts
        
    
        
    def __str__(self):
        return self.detail

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self, user, detail, pub_date):
        self.user = user
        self.detail = detail
        self.save()
    
    
class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField(max_length=100)
    
    class Meta:
        ordering = ["-pk"]
        
    def __str__(self):
        return self.comment
    
class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='business')
    contact = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    @classmethod
    def get_post(request, id):
        try:
            post = Business.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return post
    
    @classmethod
    def search_business(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses
    
    class Meta:
        ordering = ["-pk"]
    
    
    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self, name, user, contact, location, description):
        self.name = name
        self.user = user
        self.contact = contact
        self.location = location
        self.description = description
        self.save()


    
class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    priority = models.CharField( max_length=15, choices=PRIORITY)
    message = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        ordering = ["-pk"]
        
    def __str__(self):
        return self.message

    def create_alert(self):
        self.save()

    def delete_alert(self):
        self.delete()

    def update_alert(self, user, priority, message, pub_date):
        self.user = user
        self.priority = priority
        self.message = message
        self.pub_date = pub_date
        self.save()
    
        
    
    
    
