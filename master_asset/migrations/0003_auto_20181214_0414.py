# Generated by Django 2.1.4 on 2018-12-14 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_asset', '0002_auto_20181213_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='departement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement'),
        ),
    ]
