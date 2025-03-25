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
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, password=password, username=username)
        if user is not None:
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


@login_required_decorator
def faculty_create(request):
    model = Faculties()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("faculty_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "faculty/form.html", ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculties.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("faculty_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "faculty/form.html", ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculties.objects.get(pk=pk)
    model.delete()
    return redirect("faculty_list")


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, "faculty/list.html", ctx)


@login_required_decorator
def chair_create(request):
    model = Chairs()
    form = ChairForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get("actions", [])
        actions += [f"You created: "]
        request.session["actions"] = actions

        chair_count = request.session.get("chair_count", 0)
        chair_count += 1
        request.session["chair_count"] = chair_count

        return redirect("chair_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "chair/form.html", ctx)


@login_required_decorator
def chair_edit(request, pk):
    model = Chairs.objects.get(pk=pk)
    form = ChairForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get("actions", [])
        actions += ["You edited chair: "]
        request.session["actions"] = actions

        return redirect("chair_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "chair/form.html", ctx)


@login_required_decorator
def chair_delete(request, pk):
    model = Chairs.objects.get(pk=pk)
    model.delete()
    return redirect("chair_list")


@login_required_decorator
def chair_list(request):
    chairs = services.get_chairs()
    print(chairs)
    ctx = {
        "chairs": chairs
    }
    return render(request, "chair/list.html", ctx)


@login_required_decorator
def subject_create(request):
    model = Subjects()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("subject_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "subject/form.html", ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subjects.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("subject_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "subject/form.html", ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subjects.objects.get(pk=pk)
    model.delete()
    return redirect("subject_list")


@login_required_decorator
def subject_list(request):
    subjects = services.get_subjects()
    print(subjects)
    ctx = {
        "subjects": subjects
    }
    return render(request, "subject/list.html", ctx)


@login_required_decorator
def group_create(request):
    model = Groups()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("group_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "group/form.html", ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Groups.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("group_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "group/form.html", ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Groups.objects.get(pk=pk)
    model.delete()
    return redirect("group_list")


@login_required_decorator
def group_list(request):
    groups = services.get_groups()
    print(groups)
    ctx = {
        "groups": groups
    }
    return render(request, "group/list.html", ctx)


@login_required_decorator
def teacher_create(request):
    model = Teachers()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teacher_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "teacher/form.html", ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teachers.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teacher_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "teacher/form.html", ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teachers.objects.get(pk=pk)
    model.delete()
    return redirect("teacher_list")


@login_required_decorator
def teacher_list(request):
    teachers = services.get_teachers()
    print(teachers)
    ctx = {
        "teachers": teachers
    }
    return render(request, "teacher/list.html", ctx)


@login_required_decorator
def student_create(request):
    model = Students()
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("student_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "student/form.html", ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Students.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("student_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "student/form.html", ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Students.objects.get(pk=pk)
    model.delete()
    return redirect("student_list")


@login_required_decorator
def student_list(request):
    students = services.get_students()
    print(students)
    ctx = {
        "students": students
    }
    return render(request, "student/list.html", ctx)


@login_required_decorator
def profile(request):
    return render(request, 'profile.html')
