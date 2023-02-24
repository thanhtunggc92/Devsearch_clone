from django.shortcuts import render ,redirect
from .models import Projects,Tags,Reviews
from .forms import ProjectForm
# Create your views here.



def home(request):
    context={}
    return render(request,'main.html',context)
def projects(request):
    projects = Projects.objects.all()
    context = {'projects':projects}

    return render(request,'projects/projects.html',context=context)

def single_project(request,pk):
    if pk:
        project= Projects.objects.get(id=pk)
        # tags= project.objects.all()
        context= {'project':project}
        
        return render(request,'projects/single_project.html',context)

def create(request):
    form = ProjectForm

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    
    context={'form':form}

    return render(request,'projects/project_form.html',context)

def update(request,pk):
    project_id= Projects.objects.get(id=pk)
    form = ProjectForm(instance=project_id) # tell us which project need to update

    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=project_id)
        if form.is_valid():
            form.save()
            return redirect('projects')

    
    context={'form':form}

    return render(request,'projects/project_form.html',context)