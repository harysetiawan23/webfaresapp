# Generated by Django 2.1.4 on 2018-12-29 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_asset', '0005_auto_20181214_0428'),
        ('master_jadwal', '0008_auto_20181215_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamteaching',
            name='subjectId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master_asset.subject'),
        ),
    ]
