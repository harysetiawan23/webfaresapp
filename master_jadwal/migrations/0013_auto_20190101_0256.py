# Generated by Django 2.1.4 on 2019-01-01 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_jadwal', '0012_auto_20190101_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtteamteaching',
            name='faresUserId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
