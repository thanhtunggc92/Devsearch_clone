from django.shortcuts import render ,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
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


def LoginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Users does not exits')

        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request,'User or Password is incorrect')
    return render(request,'users/login_signup.html')

def logoutPage(request):
    logout(request)
    messages.success(request,'User is loggouted.')
    return redirect ('login')


def signupPage(request):
    page='signup'
    form =  SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()

            messages.success(request,'User has been created')
            login(request,user)
            return redirect('login')
        else:
            messages.error(request,'An Error during register process')
   
    context={'page':page,'form':form}
    return render(request,'users/login_signup.html',context)