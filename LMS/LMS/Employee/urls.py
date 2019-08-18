"""Employee URL Configuration"""
from django.conf.urls import url
from .views import welcome, employees

urlpatterns = [
    url(r'employees', employees),
    url(r'^$', welcome)
]
