from django.urls import path
from . import views


urlpatterns=[
    path('', views.ProfileView, name='profile'),
    path('<str:pk>/',views.UserProfile, name= 'user-profile'),
    path('login/',views.LoginPage, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('signup/',views.signupPage,name='signup'),
    path('user',views.userAccount,name='user'),
    path('user/edit',views.editUser,name="edit-user"),
    path('skills/create/',views.createSkills, name= 'skill-create'),
    path('skills/update/<str:pk>',views.updateSkills, name= 'skill-update'),
     path('skills/delete/<str:pk>',views.deleteSkills, name= 'skill-delete'),
] 