from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name= 'home'),
    path('projects',views.projects,name= 'projects'),
    path('projects/<str:pk>/',views.single_project, name='single-project'),
    path('projects/create/',views.create, name='project-create'),
    path('projects/update/<str:pk>/',views.update, name= 'project-update'),
]