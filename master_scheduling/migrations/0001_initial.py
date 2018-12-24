# Generated by Django 2.1.4 on 2018-12-12 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master_asset', '0001_initial'),
        ('master_jadwal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departementId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.student')),
                ('subjectOfferId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_jadwal.subject_offer')),
            ],
        ),
    ]
