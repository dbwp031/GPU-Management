# Generated by Django 3.2.9 on 2021-12-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makechart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
