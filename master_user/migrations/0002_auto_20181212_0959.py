# Generated by Django 2.1.4 on 2018-12-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faresuser',
            name='date_of_birth',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
