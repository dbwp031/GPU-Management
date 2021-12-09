from django.db import models
from django.db.models.fields import CharField
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=45,unique=True,primary_key=True, null=False)
    password = models.CharField(max_length=45,null=False)
    name = models.CharField(max_length=45,null=False)
    position = models.CharField(max_length=45,null=False)
    isAdmin = models.BooleanField(default=False)
    num_gpus = models.PositiveSmallIntegerField(default=0,null=False) # IntergerField => PositiveSmallIntegerField
    # requests_sent = models.CharField(max_length=45,null=False)
    # joined_projects = models.ManyToManyField("getproject.project",blank=True)