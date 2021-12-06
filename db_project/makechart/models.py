from django.db import models
from django.db.models.fields import CharField
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=300)
    rank = models.IntegerField()