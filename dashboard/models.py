from django.db import models


class Faculties(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Chairs(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculties, null=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Groups(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculties, null=False, on_delete=models.SET_NULL)
    chair = models.ForeignKey(Chairs, null=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)


class Students(models.Model):
    objects = None
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField()
    group = models.ForeignKey(Groups, null=False, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teachers(models.Model):
    objects = None
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField()
    subject = models.ForeignKey(Subjects, null=False, on_delete=models.SET_NULL)
    chair = models.ForeignKey(Chairs, null=False, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
