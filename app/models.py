from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    fee = models.IntegerField()
    Duration = models.IntegerField()