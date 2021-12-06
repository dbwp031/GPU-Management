# Generated by Django 3.2.9 on 2021-12-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=45, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=45)),
                ('num_gpus', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]