
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import ProjectSerializers
from projects.models import Project,Reviews
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def getRouts(request):

    routs = [
        {'GET':'api/projects'},
         {'GET':'api/projects/id'},
         {'POST':'api/projects/id/vote'},
         {'POST':'api/users/token'},
         {'POST':'api/users/token/refresh'},
         
    ]
    return Response(routs)

@api_view(['GET'])
def getProjects(request):
    projects= Project.objects.all()
    serializer= ProjectSerializers(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSingleProject(request,pk):
    single_project= Project.objects.get(id=pk)
    serializer= ProjectSerializers(single_project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ProjectVote(request,pk):

    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    print('Data:',data)
    review, created = Reviews.objects.get_or_create(
        owner_name = user,
        project = project,
    )
    review.value = data['value']
    review.save()
    project.getVoteCount
    serializer = ProjectSerializers(project, many=False)
    return Response(serializer.data)
