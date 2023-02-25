from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.projects,name= 'projects'),
    path('projects/<uuid:pk>/',views.single_project, name='single-project'),
    path('projects/create/',views.create, name='project-create'),
    path('projects/update/<str:pk>/',views.update, name= 'project-update'),
    path('projects/delete/<str:pk>/',views.delete, name= 'project-delete'),
]