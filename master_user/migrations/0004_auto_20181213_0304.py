# Generated by Django 2.1.4 on 2018-12-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_user', '0003_auto_20181212_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faresuser',
            name='isMale',
        ),
        migrations.AddField(
            model_name='faresuser',
            name='gender',
            field=models.IntegerField(default=True, null=True),
        ),
    ]
