
from django.urls import path
from . import views
from EmployeeApp import views


urlpatterns=[
    #path('department/', views.department, name='department'),
    path('department/',views.departmentApi),
    path('department/([0-9]+)$',views.departmentApi),

    path('employee/',views.employeeApi),
    path('employee/([0-9]+)$',views.employeeApi),

    path('SaveFile/', views.SaveFile)

] 
