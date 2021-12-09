from django.db import models
from django.db.models.fields import CharField
from getuser.models import User
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=300)
    rank = models.IntegerField()
    ranks = models.IntegerField()
    
    
class GPU(models.Model):
    gpu_id = models.CharField(max_length=45,primary_key=True,null=False)
    tpe = models.CharField(max_length=45,null=False)
    location = models.CharField(max_length=45,null=False)
    # year_of_purchase = models.DateField
    vendor = models.CharField(max_length=45,null=False)
    
    # 외래 키
    gpu_users = models.ForeignKey("getuser.User",on_delete=models.CASCADE,blank=True,null=True)#,related_name="user_id")