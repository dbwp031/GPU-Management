# Generated by Django 3.2.5 on 2021-12-08 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getuser', '0006_alter_user_joined_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='joined_projects',
        ),
    ]