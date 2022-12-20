from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import TaskSerializer
from task.models import Task



@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/tasks'},
        {'GET': '/api/tasks/id'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

        {'POST': '/api/tasks/update/id'},
        {'DELETE': '/api/tasks/delete/id'},
    ]

    return Response(routes)


# returning all the tasks

@api_view(['GET'])
def getTasks(request):
    print("USER:", request.user)
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data)



# returning one single task

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewTask(request, pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializer(task, many=False)
    return Response(serializers.data)


# This is not working...: can't generate uuid for task through api

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def createTask(request):
#    serializer = TaskSerializer(data=request.data)
#    if serializer.is_valid():
#        serializer.save()

#    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Deleted')
    
