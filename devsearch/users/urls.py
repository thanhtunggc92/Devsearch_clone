from django.urls import path
from . import views


urlpatterns=[
    path('', views.ProfileView, name='profile'),
    path('<uuid:pk>/',views.UserProfile, name= 'user-profile'),
    path('login/',views.LoginPage, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('signup/',views.signupPage,name='signup'),
]