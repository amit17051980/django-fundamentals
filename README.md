Django Fundamentals
===================

This repository has been created to explore the Django framework, and at the
same time sharing the work done with other community members.

Work Instructions [Linux (Ubuntu-18)]
-------------------------------------

Although this document is referring Linux only, it is also possible to run this
on windows by searching equivalent dependencies. I have found it a bit difficult
to work on Windows due to lack of support when you hit issues with dependencies,
e.g., xmlsec1.exe and associated DLLs.

### Install Python3 and Dependencies 

Github Path :
<https://github.com/amit17051980/django-fundamentals/blob/development/LMS/LMS/Setup-Ubuntu-Pkg.sh>

### Install LiClipse for Linux 64 bit

Download Link :
<https://www.mediafire.com/file/63ixawa1panjfny/liclipse_5.2.4_linux.gtk.x86_64.tar.gz>

Instructions : <http://www.liclipse.com/download.html#linux>

### Create Python Virtual Environment

Use Instructions : <https://docs.python.org/3/library/venv.html>

>   mkdir Python_Virtual_Envs

>   cd Python_Virtual_Envs/

>   mkdir django-fundamentals

>   cd django-fundamentals/

>   python3 -m venv .

### Setup LiClipse for Virtual Environment

Use Instructions: <https://www.pydev.org/manual_101_interpreter.html>

### Install PIP Dependencies

1.  Activate the Virtual Environment (CMD) or use Windows Preferences
    Interpreters Python (manage with pip)

2.  Run command below:

>   pip install -r
>   <https://github.com/amit17051980/django-fundamentals/blob/development/LMS/LMS/requirements.txt>
