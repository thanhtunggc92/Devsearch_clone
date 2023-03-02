from django.db.models import Q
from .models import Skill,Profile
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def paginationFunction(request,profiles,result):

    page =request.GET.get('page')
    # result= 2
    paginator = Paginator(profiles,result)
    try : 
       
        projects = paginator.page(page)
    except PageNotAnInteger:
        page= 1
        profiles = paginator.page(page)

    except EmptyPage:
        page = paginator.projects.number()
        profiles= paginator.page(page)
    return profiles ,paginator


def searchProfiles(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)|
        Q(short_intro__icontains=search_query)|
        Q(skill__in=skills)
        )
    return profiles,search_query
