# Generated by Django 3.2.5 on 2021-12-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getuser', '0005_user_joined_projects'),
        ('getproject', '0002_rename_student_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='participants_id',
            field=models.ManyToManyField(blank=True, to='getuser.User'),
        ),
    ]
