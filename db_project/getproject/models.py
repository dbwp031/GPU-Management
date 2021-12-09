from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.CharField(max_length=45,primary_key=True,null=False)
    partners = models.CharField(max_length=45,null=False)
    details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    
    participants_id = models.ManyToManyField("getuser.User",blank=True)