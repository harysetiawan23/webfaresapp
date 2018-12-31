from django.db import models

# Create your models here.

from master_asset.models import teacher, shift, subject, classRoom, student, departement
from master_user.models import FaresUser


class teamTeaching(models.Model):
    name = models.CharField(max_length=20)
    deptId = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        null=True
    )
    subjectId = models.ForeignKey(
        subject,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return "[ %s / %s ] %s " % (self.deptId.name, self.deptId.unit_id.name, self.name)


class dtTeamTeaching(models.Model):
    teamId = models.ForeignKey(
        teamTeaching,
        null=True,
        on_delete=models.CASCADE
    )
    faresUserId = models.ForeignKey(
        FaresUser,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return "[ %s / %s ] %s - %s %s " % (
            self.teamId.deptId.name, self.faresUserId.dept_id.unit_id.name, self.teamId.name,
            self.faresUserId.registred_no,
            self.faresUserId.full_name)


class time(models.Model):
    DAYS = (
        (0, 'Minggu'),
        (1, 'Senin'),
        (2, 'Selasa'),
        (3, 'Rabu'),
        (4, 'Kamis'),
        (5, 'Jumat'),
        (6, 'Sabtu'),

    )
    day = models.IntegerField(default=True, choices=DAYS)
    hour_start = models.TimeField(null=True)
    hour_stop = models.TimeField(null=True)
    shift_id = models.ForeignKey(
        shift,
        on_delete=models.CASCADE,
        null=True
    )
    departementId = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
        return "[ %s ] %s %s - %s " % (
            self.departementId, days[self.day], self.hour_start, self.hour_stop)


class subject_offer(models.Model):
    teamTeaching_id = models.ForeignKey(
        teamTeaching,
        on_delete=models.CASCADE,
        null=True
    )
    subject_id = models.ForeignKey(
        subject,
        on_delete=models.CASCADE,
        null=True
    )
    classRoomId = models.ForeignKey(
        classRoom,
        on_delete=models.CASCADE,
        null=True
    )
    time_id = models.ForeignKey(
        time,
        on_delete=models.CASCADE,
        null=True
    )
    semester = models.CharField(max_length=10, null=True)
    school_year = models.CharField(max_length=10, null=True)
    departement = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        null=True
    )

    # def __str__(self):
    #     return "[ %s / %s ] [ %s - %s ] - %s" % (
    #     self.departement.name, self.departement.unit_id.name, self.school_year, self.semester, self.subject_id)


class absence(models.Model):
    subjectOfferId = models.ForeignKey(
        subject_offer,
        on_delete=models.CASCADE
    )
    timeStart = models.TimeField(auto_now_add=True)
    timeStop = models.TimeField(null=True)
    notes = models.TextField()
    lng = models.TextField()
    lat = models.TextField()
    classType = models.BooleanField()
    absenceType = models.BooleanField()
    departement = models.ForeignKey(
        departement,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "[ %s - %s ] [ %s %s - %s ] - %s " % (
            self.departement.name, self.departement.unit_id.name, self.subjectOfferId.classRoomId.class_name,
            self.timeStart, self.timeStop, self.subjectOfferId.subject_id.name)


class dtAbsence(models.Model):
    absenceId = models.ForeignKey(
        absence,
        on_delete=models.CASCADE
    )
    studentId = models.ForeignKey(
        student,
        on_delete=models.CASCADE
    )
    timeIn = models.TimeField(auto_now_add=True, null=True)
    isPresent = models.BooleanField(default=False)
    lng = models.TextField()
    lat = models.TextField()
    departement = models.ForeignKey(
        departement,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "[ %s - %s ] [ %s %s - %s ] - %s " % (
            self.departement.name, self.departement.unit_id.name, self.absenceId.subjectOfferId.classRoomId.class_name,
            self.timeIn, self.absenceId.subjectOfferId.subject_id.name, self.studentId.full_name)
