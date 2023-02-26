from django.urls import path
from . import views


urlpatterns=[
    path('', views.ProfileView, name='profile'),
    path('<str:pk>/',views.UserProfile, name= 'user-profile'),
]