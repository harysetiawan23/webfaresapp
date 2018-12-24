# Generated by Django 2.1.4 on 2018-12-14 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_jadwal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='departement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement'),
        ),
        migrations.AlterField(
            model_name='time',
            name='hour_start',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='hour_stop',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='shift_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master_asset.shift'),
        ),
    ]