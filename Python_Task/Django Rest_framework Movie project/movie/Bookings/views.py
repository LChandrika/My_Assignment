
from django.shortcuts import render
from.models import Movie
from.Serializers import Movieserializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def Movie_data(request):
    if request.method=='GET':
        cinema=Movie.objects.all()
        serializer=Movieserializer(cinema,many=True)
        return JsonResponse(serializer.data,status=status.HTTP_202_ACCEPTED,safe=False)
    if request.method=='POST':
        serializer=Movieserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Movie_details(request,id):
    try:
        cinema=Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Movieserializer(cinema)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        serializer=Movieserializer(cinema,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        cinema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


