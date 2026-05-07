from django.db import models

# Create your models here.
class HomeWork(models.Model):
    subject = models.CharField(max_length=100)
    question = models.CharField(max_length=300)
    submit_date= models.DateField()