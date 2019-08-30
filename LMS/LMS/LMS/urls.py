"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
import django_saml2_auth.views

urlpatterns = [
    url(r'^saml2_auth/', include('django_saml2_auth.urls')),
    url(r'^accounts/login/$', django_saml2_auth.views.signin),
    url(r'^admin/login/$', django_saml2_auth.views.signin),
    url(r'^accounts/logout/$', django_saml2_auth.views.signout),
    url(r'^admin/logout/$', django_saml2_auth.views.signout),
    
    path('admin/', admin.site.urls),
    url('employee/', include('Employee.urls')),
]
