from django.db.models import Q
from .models import Project,Tags
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def paginationFunction(request,projects,result):

    page =request.GET.get('page')
    # result= 2
    paginator = Paginator(projects,result)
    try : 
       
        projects = paginator.page(page)
    except PageNotAnInteger:
        page= 1
        projects = paginator.page(page)

    except EmptyPage:
        page = paginator.projects.number()
        projects= paginator.page(page)
    return projects ,paginator
def searchProjects(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags= Tags.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(descriptions__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tags)
    )
    return projects,search_query