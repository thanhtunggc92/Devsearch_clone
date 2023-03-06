from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.getRouts),
    path('projects/',views.getProjects),
    path('projects/<str:pk>/',views.getSingleProject),
    path('projects/<str:pk>/vote/',views.ProjectVote),
    path('remove-tag/',views.removeTag)
]