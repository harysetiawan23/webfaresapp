# Generated by Django 2.1.4 on 2019-01-01 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_jadwal', '0011_auto_20181231_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtteamteaching',
            name='teamId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master_jadwal.teamTeaching'),
        ),
    ]
