from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Faculties, Groups, Chairs, Students, Teachers, Subjects
from .forms import FacultyForm, ChairForm, StudentForm, SubjectForm, TeacherForm, GroupForm
from . import services


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username ")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            login(request, user)
            return redirect("home_page")

    return render(request, "login.html")


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    chairs = services.get_chairs()
    groups = services.get_groups()
    subjects = services.get_subjects()
    students = services.get_students()
    teachers = services.get_teachers()
    ctx = {
        "faculties": len(faculties),
        "chairs": len(chairs),
        "groups": len(groups),
        "subjects": len(subjects),
        "students": len(students),
        "teachers": len(teachers)
    }
    return render(request, "index.html", ctx)

