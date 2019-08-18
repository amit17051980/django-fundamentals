from Employee.models import Employee
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, "base.html")


# Create your views here.
def employees(request):
    employees = Employee.objects.zero_manager()
    return render(request, "Employee/employees.html", {'employees':employees})

