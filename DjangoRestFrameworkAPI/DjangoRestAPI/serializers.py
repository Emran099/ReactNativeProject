# Python Object to JSON

from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
         model = Drink
         fields = ('id','name','description')
   
    


#Serializer to JSON TO DB OR DB TO JSON

# from rest_framework import serializers
# from EmployeeApp.models import  Departments, Employees

# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departments
#         fields = ('DepartmentId',
#                   'DepartmentName')
        
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employees
#         fields = ('EmployeeId',
#                   'EmployeeName',
#                   'Department',
#                   'DateOfJoining',
#                   'PhotoFileName')


