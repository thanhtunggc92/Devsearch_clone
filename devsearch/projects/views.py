from django.shortcuts import render ,redirect
from .models import Project,Tags,Reviews
from .forms import ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects, paginationFunction
from django.contrib import messages

# Create your views here.




def projects(request):
   
    projects,search_query = searchProjects(request)
    projects,paginator=paginationFunction(request,projects,3)
   
    context = {'projects':projects,'search_query':search_query,'paginator':paginator}

    return render(request,'projects/projects.html',context=context)

def single_project(request,pk):
    
        projectobj= Project.objects.get(id=pk)
        form=ReviewForm()
        # tags= project.objects.all()
        if request.method == 'POST':
            form =ReviewForm(request.POST)
            if form.is_valid:
                review=form.save(commit=False)
                review.project = projectobj
                review.owner_name = request.user.profile
                review.save()
                projectobj.getVoteCount
                messages.success(request,'Your review was successfully submitted')
                return redirect('single-project', pk = projectobj.id)
            
        context= {'project':projectobj, 'form':form}
        return render(request,'projects/single_project.html',context)
@login_required(login_url='login')
def create(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags= request.POST.get('newtags').replace(','," ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project= form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag,created = Tags.objects.get_or_create(
                    name=tag
                )
                project.tags.add(tag)
            return redirect('user')

    
    context={'form':form}

    return render(request,'projects/project_form.html',context)
@login_required(login_url='login')
def update(request,pk):
    profile = request.user.profile

    project= profile.project_set.get(id=pk)

    form = ProjectForm(instance=project) # tell us which project need to update

    if request.method == 'POST':
        newtags= request.POST.get('newtags').replace(','," ").split()
       
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag,created = Tags.objects.get_or_create(
                    name=tag
                )
                project.tags.add(tag)
            return redirect('projects')

    
    context={'form':form , 'project':project}

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