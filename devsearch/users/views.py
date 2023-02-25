from django.shortcuts import render

# Create your views here.


def Profile(request):
    context={}

    return render(request,'users/profile.html',context)