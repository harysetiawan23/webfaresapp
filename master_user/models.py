from django.db import models
from django.contrib.auth.models import AbstractUser
from master_asset.models import departement

# Create your models here.

class FaresUser(AbstractUser):
    registred_no = models.CharField(max_length=25, null=False)
    full_name = models.CharField(max_length=50, null=False)
    nick_name = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    username = models.CharField(max_length=25, unique=True)
    password = models.TextField(null=False)
    gender = models.IntegerField(null=True, default=True)
    address = models.TextField(null=True)
    photo = models.TextField(null=True)
    year = models.IntegerField(null=True)
    dept_id = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        null=True
    )

    isTeacher = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.pk

    def __iter__(self):
        return [
            self.registred_no,
            self.first_name,
            self.nick_name,
            self.gender,
            self.date_of_birth,
            self.photo,
            self.dept_id_id]
