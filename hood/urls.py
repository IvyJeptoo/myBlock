from django.urls import path,include
from neibourhood import views
from .views import *

urlpatterns=[
    path('',views.index),
    path('register/',RegisterView.as_View(),name='users-register'),
    path('home',views.home, name='home'),
    path('viewProfile',views.viewProfile, name='viewProfile'),
    path('comment',views.comment, name='comment'),
    
]