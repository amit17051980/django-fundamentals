from Employee.models import Employee
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
    return render(request, "base.html")


# Create your views here.
@login_required
def employees(request):
    employees = Employee.objects.zero_manager()
    return render(request, "Employee/employees.html", {'employees':employees})

