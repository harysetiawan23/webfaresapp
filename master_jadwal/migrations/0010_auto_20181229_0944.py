# Generated by Django 2.1.4 on 2018-12-29 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_jadwal', '0009_teamteaching_subjectid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='departement',
            new_name='departementId',
        ),
    ]
