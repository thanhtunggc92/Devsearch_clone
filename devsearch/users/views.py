from django.shortcuts import render ,redirect
from .models import Profile,Message
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm,ProfileForm ,UserSkill,MessageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles,paginationFunction
# Create your views here.




def ProfileView(request):
  
    # profiles = Profile.objects.all()
    profiles , search_query = searchProfiles(request)
    profiles,paginator =paginationFunction(request,profiles,1)
    context={'profiles':profiles,'search_query':search_query,'paginator':paginator}

    return render(request,'users/profile.html',context)


def UserProfile(request,pk):

    profile =  Profile.objects.get(id=pk)
   
       
    topSkills = profile.skill_set.exclude(descriptions__exact="")
    otherSkills = profile.skill_set.filter(descriptions="")
    context = {'profile':profile, 'topskills':topSkills,'otherskills':otherSkills}
    return render(request, 'users/user_profile.html',context)

def LoginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        print(request.POST)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Users does not exits')

        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'user')
            
        else:
            messages.error(request,'User or Password is incorrect')
    return render(request,'users/login_signup.html')

def logoutPage(request):
    logout(request)
    messages.info(request,'User is loggouted.')
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


@login_required(login_url='login')
def userAccount(request):
    profile= request.user.profile
    skills = profile.skill_set.all()  # query a skill in data with many to many relationship
    projects= profile.project_set.all()
    context= {'profile':profile, 'skills':skills, 'projects':projects}
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editUser(request):
    profile = request.user.profile
    form =ProfileForm(instance=profile)
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user')
    context={'form':form}
    return render(request,'users/user_form.html',context)

@login_required(login_url='login')
def createSkills(request):
    profile = request.user.profile
    form = UserSkill()
    if request.method =='POST':
        form = UserSkill(request.POST)
        skill = form.save(commit=False)
        skill.owner = profile
        skill.save()
        messages.success(request,'Your skills was added')
        return redirect('user')
    context = {'form':form}

    return render(request,'users/skill_form.html',context)

@login_required(login_url='login')
def updateSkills(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = UserSkill()
    if request.method =='POST':
        form = UserSkill(request.POST,instance=skill)
       
        form.save()
        messages.success(request,'You are successfully update your skills')
        return redirect('user')
    context = {'form':form}

    return render(request,'users/skill_form.html',context)


@login_required(login_url='login')
def deleteSkills(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method =='POST':
        skill.delete()
        messages.success(request,'Skill was deleted successfully')
        return redirect('user')
    context = {'object':skill}
    return render(request,'delete.html',context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    mess = profile.messages.all()
    unread_mess= mess.filter(is_read =False).count()
    context={'message':mess,'unread_mess':unread_mess}
    return render(request,'users/inbox.html',context)

@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    message_id = profile.messages.get(id=pk)
    if message_id.is_read == False:
        message_id.is_read = True
        message_id.save()
    context={'message':message_id}


    return render(request,'users/message.html',context)

def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    print(recipient)
    form = MessageForm()
    try:
        sender  = request.user.profile
    except:
        sender =None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            messages.success(request,'You message has successfully sent!!')
            return redirect('user-profile', pk=recipient.id)
    context={'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',context)