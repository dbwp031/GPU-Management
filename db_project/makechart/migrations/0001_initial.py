# Generated by Django 3.2.5 on 2021-12-08 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('getuser', '0004_alter_user_isadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('gpu_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('tpe', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=45)),
                ('vendor', models.CharField(max_length=45)),
                ('gpu_users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='getuser.user')),
            ],
        ),
    ]
