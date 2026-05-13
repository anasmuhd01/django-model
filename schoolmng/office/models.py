from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100)
    hod=models.CharField(max_length=100)
    dept_room=models.CharField(max_length=50)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=30)
    place = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="Teacher_photos")