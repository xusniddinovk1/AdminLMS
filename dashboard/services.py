from django.db import connection
from contextlib import closing


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor) as cursor:
        cursor.execute("""SELECT * FROM dashboard_faculties""")
        faculties = dict_fetchall(cursor)
        return faculties


def get_chairs():
    with closing(connection.cursor) as cursor:
        cursor.execute("""SELECT * FROM dashboard_chairs""")
        chairs = dict_fetchall(cursor)
        return chairs


def get_groups():
    with closing(connection.cursor) as cursor:
        cursor.execute("""SELECT dashboard_groups.id, dashboard_groups.name, dashboard_faculties.name as faculty from dashboard_groups
                                LEFT JOIN dashboard_faculties ON dashboard_faculties.id = dashboard_group.faculty_id""")
        groups = dict_fetchall(cursor)
        return groups


def get_subjects():
    with closing(connection.cursor) as cursor:
        cursor.execute("""SELECT * FROM dashboard_subject""")
        subjects = dict_fetchall(cursor)
        return subjects


def get_teachers():
    with closing(connection.cursor) as cursor:
        cursor.execute("""SELECT dashboard_teachers.id, dashboard_teachers.first_name, dashboard_teachers.last_name, dashboard_teachers.age,
                    dashboard_chairs.name as chair_name, dashboard_subjects.name as subject_name, FROM dashboard_subjects
                    LEFT JOIN dashboard_chairs ON dashboard_teachers.chair_id = dashboard_chairs.id LEFT JOIN dashboard_subjects
                    ON dashboard_teachers.subject_id = dashboard_subjects.id""")
        teachers = dict_fetchall(cursor)
        return teachers


def get_students():
    with closing(connection.cursor) as cursor:
        cursor.execute("""SELECT dashboard_students.first_name, dashboard_students.last_name, dashboard_students.age,
                    dashboard_students.image as image, dashboard_groups.name as group_name FROM dashboard_students LEFT JOIN dashboard_students
                    ON dashboard_groups ON dashboard_groups.id = dashboard_students.group_id""")
        students = dict_fetchall(cursor)
        return students
