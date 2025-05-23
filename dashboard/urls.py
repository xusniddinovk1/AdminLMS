from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home_page"),
    path("logout/", logout_page, name="logout_page"),
    path("login/", login_page, name="login_page"),

    path("faculty/create/", faculty_create, name="faculty_create"),
    path("faculty/<int:pk>/edit/", faculty_edit, name="faculty_edit"),
    path("faculty/<int:pk>/delete/", faculty_delete, name="faculty_delete"),
    path("faculty/list/", faculty_list, name="faculty_list"),

    path("chair/create/", chair_create, name="chair_create"),
    path("chair/<int:pk>/edit/", chair_edit, name="chair_edit"),
    path("chair/<int:pk>/delete/", chair_delete, name="chair_delete"),
    path("chair/list/", chair_list, name="chair_list"),

    path("subject/create/", subject_create, name="subject_create"),
    path("subject/<int:pk>/edit/", subject_edit, name="subject_edit"),
    path("faculty/<int:pk>/delete/", faculty_delete, name="subject_delete"),
    path("subject/list/", subject_list, name="subject_list"),

    path('group/create/', group_create, name='group_create'),
    path('group/<int:pk>edit/', group_edit, name='group_edit'),
    path('group/<int:pk>/delete/', group_delete, name='group_delete'),
    path('group/list/', group_list, name='group_list'),

    path('teacher/create/', teacher_create, name='teacher_create'),
    path('teacher/<int:pk>edit/', teacher_edit, name='teacher_edit'),
    path('teacher/<int:pk>/delete/', teacher_delete, name='teacher_delete'),
    path('teacher/list/', teacher_list, name='teacher_list'),

    path('student/create/', student_create, name='student_create'),
    path('student/<int:pk>edit/', student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', student_delete, name='student_delete'),
    path('student/list/', student_list, name='student_list'),

    path('profile/', profile, name='profile')

]