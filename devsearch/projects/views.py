from django.shortcuts import render ,redirect
from .models import Project,Tags,Reviews
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects, paginationFunction

# Create your views here.




def projects(request):
    # search_query = ''
    
    # if request.GET.get('search_query'):
    #     search_query = request.GET.get('search_query')
    # tags= Tags.objects.filter(name__icontains=search_query)
    # projects = Project.objects.distinct().filter(
    #     Q(title__icontains=search_query)|
    #     Q(descriptions__icontains=search_query)|
    #     Q(owner__name__icontains=search_query)|
    #     Q(tags__in=tags)
    # )
    # projects = Project.objects.all()
    projects,search_query = searchProjects(request)
    projects,paginator=paginationFunction(request,projects,3)
   
    context = {'projects':projects,'search_query':search_query,'paginator':paginator}

    return render(request,'projects/projects.html',context=context)

def single_project(request,pk):
  
        project= Project.objects.get(id=pk)
        # tags= project.objects.all()
        context= {'project':project}
        
        return render(request,'projects/single_project.html',context)
@login_required(login_url='login')
def create(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project= form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    
    context={'form':form}

    return render(request,'projects/project_form.html',context)
@login_required(login_url='login')
def update(request,pk):
    profile = request.user.profile

    project_id= profile.project_set.get(id=pk)
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
    profile = request.user.profile
    project_id= profile.project_set.get(id=pk)
    if request.method == 'POST':
        project_id.delete()
        return redirect('projects')
    context ={'object':project_id}
    return render(request,'delete.html',context)