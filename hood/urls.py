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
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('visit',views.visit, name='visit'),


    # path('alert',views.alert, name='alert'),
    # path('post',views.post, name='post'),
    # path('business',views.business, name='business'),
    
    
    
]