from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .serializers import Employee_serializers
# Create your views here.

class Employee_details(APIView):
    def get(self,request):
        obj = Employee.objects.all()
        serialzier = Employee_serializers(obj, many = True)
        return Response(serialzier.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = Employee_serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class Employee_info(APIView):
    def get(self,request,id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {"msg":"Not Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = Employee_serializers(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
     
    def put(self,request,id):
        try:
            obj = Employee.objects.get(id = id)
        except Employee.DoesNotExist:
            msg = {"msg":"Not Found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = Employee_serializers(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            obj = Employee.objects.get(id = id)

        except Employee.DoesNotExist:
            msg = {"msg":"NotFound"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"delete"},status=status.HTTP_204_NO_CONTENT)
