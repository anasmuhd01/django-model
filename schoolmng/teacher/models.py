from django.db import models

# Create your models here.
class StudentList(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    batch = models.CharField(max_length=50)
    place = models.CharField(max_length=100)