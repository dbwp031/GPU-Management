# Generated by Django 3.2.9 on 2021-12-06 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getuser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
    ]