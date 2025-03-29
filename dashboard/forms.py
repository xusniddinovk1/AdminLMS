from .models import Faculties, Chairs, Groups, Students, Teachers
from django import forms


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculties
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }


class ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "faculty": forms.Select(attrs={"class": "form-control"}),
            "chair": forms.Select(attrs={"class": "form-control"}),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "chair": forms.TextInput(attrs={"class": "form-control"})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "group": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})
        }
