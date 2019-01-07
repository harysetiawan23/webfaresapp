from django.db import models
from django.contrib import admin

from master_asset.models import student, departement
from master_jadwal.models import subject_offer
from master_user.models import FaresUser


class studentClass(models.Model):
    studentId = models.ForeignKey(
        FaresUser,
        on_delete=models.CASCADE,
        null=True
    )
    subjectOfferId = models.ForeignKey(
        subject_offer,
        on_delete=models.CASCADE,
        null=True
    )
    departementId = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return "[ %s / %s ] - %s %s %s" % (
        self.departementId.name, self.departementId.unit_id.name, self.subjectOfferId.subject_id.name,
        self.subjectOfferId.classRoomId.class_name, self.studentId.full_name)
