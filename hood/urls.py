from django.urls import path,include
from . import views
from .views import *

urlpatterns=[
    path('',views.index, name='index'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('home',views.home, name='home'),
    path('viewProfile',views.viewProfile, name='viewProfile'),
    path('createProfile',views.createProfile, name='createProfile'),
    path('comment/<id>',views.comment, name='comment'),
    path('searchBusiness',views.searchBusiness, name = 'searchBusiness'),
    
    
    
]