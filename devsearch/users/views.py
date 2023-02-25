from django.shortcuts import render
from .models import Profile
# Create your views here.




def ProfileView(request):
    profiles = Profile.objects.all()


    context={'profiles':profiles}

    return render(request,'users/profile.html',context)