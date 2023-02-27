from django.shortcuts import render ,redirect
from .models import Projects,Tags,Reviews
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.




def projects(request):
    projects = Projects.objects.all()
    context = {'projects':projects}

    return render(request,'projects/projects.html',context=context)

def single_project(request,pk):
  
        project= Projects.objects.get(id=pk)
        # tags= project.objects.all()
        context= {'project':project}
        
        return render(request,'projects/single_project.html',context)
@login_required(login_url='login')
def create(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    
    context={'form':form}

    return render(request,'projects/project_form.html',context)
@login_required(login_url='login')
def update(request,pk):
    project_id= Projects.objects.get(id=pk)
    print(project_id)
    form = ProjectForm(instance=project_id) # tell us which project need to update

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project_id)
        if form.is_valid():
            form.save()
            return redirect('projects')

    
    context={'form':form}

    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def delete(request,pk):
    project_id= Projects.objects.get(id=pk)
    if request.method == 'POST':
        project_id.delete()
        return redirect('projects')
    context ={'object':project_id}
    return render(request,'projects/delete.html',context)