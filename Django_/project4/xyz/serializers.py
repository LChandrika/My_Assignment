from rest_framework import serializers
from .models import Employee

class Employee_serializers(serializers.ModelSerializer):
    class Mete:
        model = Employee
        fields = "__all__" 