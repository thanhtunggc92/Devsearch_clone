from django.shortcuts import render
from .models import Profile
# Create your views here.




def ProfileView(request):
    profiles = Profile.objects.all()


    context={'profiles':profiles}

    return render(request,'users/profile.html',context)


def UserProfile(request,pk):
    profile =  Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(descriptions__exact="")
    otherSkills = profile.skill_set.filter(descriptions="")
    context = {'profile':profile, 'topskills':topSkills,'otherskills':otherSkills}
    return render(request, 'users/user-profile.html',context)