from Employee.models import Employee
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Employee.forms import InvitationForm
from .models import Invitation


# Create your views here.
def welcome(request):
    return render(request, "base.html")


# Create your views here.
@login_required
def employees(request):
    employees = Employee.objects.zero_manager()
    return render(request, "Employee/employees.html", {'employees':employees})


@login_required
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_home')
    form = InvitationForm
    return render(request, "Employee/invitation.html", {'form':form})
