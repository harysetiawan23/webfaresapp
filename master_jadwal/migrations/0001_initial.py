# Generated by Django 2.1.4 on 2018-12-12 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master_asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStart', models.TimeField(auto_now_add=True)),
                ('timeStop', models.TimeField(null=True)),
                ('notes', models.TextField()),
                ('lng', models.TextField()),
                ('lat', models.TextField()),
                ('classType', models.BooleanField()),
                ('absenceType', models.BooleanField()),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement')),
            ],
        ),
        migrations.CreateModel(
            name='dtAbsence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeIn', models.TimeField(auto_now_add=True, null=True)),
                ('isPresent', models.BooleanField(default=False)),
                ('lng', models.TextField()),
                ('lat', models.TextField()),
                ('absenceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_jadwal.absence')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.student')),
            ],
        ),
        migrations.CreateModel(
            name='dtTeamTeaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='subject_offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectOfferId', models.CharField(max_length=20, null=True)),
                ('semester', models.CharField(max_length=10, null=True)),
                ('school_year', models.CharField(max_length=10, null=True)),
                ('classRoomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.classRoom')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.subject')),
            ],
        ),
        migrations.CreateModel(
            name='teamTeaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('deptId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement')),
            ],
        ),
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Minggu'), (1, 'Senin'), (2, 'Selasa'), (3, 'Rabu'), (4, 'Kamis'), (5, 'Jumat'), (6, 'Sabtu')], default=True)),
                ('hour_start', models.TimeField()),
                ('hour_stop', models.TimeField()),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.departement')),
                ('shift_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_asset.shift')),
            ],
        ),
        migrations.AddField(
            model_name='subject_offer',
            name='teamTeaching_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_jadwal.teamTeaching'),
        ),
        migrations.AddField(
            model_name='subject_offer',
            name='time_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_jadwal.time'),
        ),
        migrations.AddField(
            model_name='dtteamteaching',
            name='teamId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_jadwal.teamTeaching'),
        ),
        migrations.AddField(
            model_name='absence',
            name='subjectOfferId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_jadwal.subject_offer'),
        ),
    ]
