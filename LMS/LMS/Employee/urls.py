"""Employee URL Configuration"""
from django.conf.urls import url

from .views import welcome, employees, new_invitation

urlpatterns = [
    url(r'employees', employees),
    url(r'invitation', new_invitation, name='employee_new_invitation'),
    url(r'^$', welcome, name='employee_home')
]
