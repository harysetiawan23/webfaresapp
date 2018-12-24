from django.db import models


# Create your models here.

#   MASTER / MANDATORY
class unit(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return "%s" % self.name


class departement(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.TextField()
    unit_id = models.ForeignKey(
        unit,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s - %s" % (self.name, self.unit_id.name)


class shift(models.Model):
    name = models.CharField(max_length=20)
    departement = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        default=True
    )

    def __str__(self):
        return "[ %s / %s ] %s " % (self.departement.name, self.departement.unit_id.name, self.name)


class religion(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.name)


#   COMMON DATA

class student(models.Model):
    ANGKATAN = (
        (2015, 2015),
        (2016, 2016),
        (2017, 2017),
        (2018, 2018),
        (2019, 2019),
        (2020, 2020),
        (2021, 2021),
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025),
        (2026, 2026),
        (2027, 2027),
        (2028, 2028),
        (2029, 2029),
        (2030, 2030),
        (2031, 2031),
    )

    student_registred_no = models.CharField(max_length=25, null=False)
    full_name = models.CharField(max_length=50, null=False)
    nick_name = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField()
    gender = models.BooleanField(default=True)
    address = models.TextField()
    photo = models.TextField()
    year = models.IntegerField( choices=ANGKATAN)
    dept_id = models.ForeignKey(
        departement,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "[ %s / %s ] %s - %s " % (
            self.dept_id.name, self.dept_id.unit_id.name, self.student_registred_no, self.full_name)


class studentFace(models.Model):
    student_id = models.ForeignKey(
        student,
        on_delete=models.CASCADE
    )
    face_function = models.TextField()

    def __str__(self):
        return "[ %s / %s ] %s - %s " % (
            self.student_id.dept_id.name, self.student_id.dept_id.unit_id.name, self.student_id.student_registred_no,
            self.student_id.full_name)


class classRoom(models.Model):
    class_name = models.CharField(max_length=10)
    departement = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return "[ %s / %s ] %s " % (self.departement.name, self.departement.unit_id.name, self.class_name)


class teacher(models.Model):
    employee_no = models.CharField(max_length=50)
    national_teacher_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    religion = models.ForeignKey(
        religion,
        on_delete=models.CASCADE
    )
    dept_id = models.ForeignKey(
        departement,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "[ %s / %s ] %s - %s" % (
            self.dept_id.name, self.dept_id.unit_id.name, self.national_teacher_number, self.full_name)


class teacherFace(models.Model):
    teacherId = models.ForeignKey(
        teacher,
        on_delete=models.CASCADE
    )

    teacher_face = models.TextField()

    def __str__(self):
        return "[ %s / %s ] %s - %s" % (
            self.teacherId.dept_id.name, self.teacherId.dept_id.unit_id.name, self.teacherId.national_teacher_number,
            self.teacherId.full_name)


class subject(models.Model):
    subject_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20)
    detail = models.TextField()
    dept_id = models.ForeignKey(
        departement,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return "[ %s / %s ] %s " % (self.dept_id.name, self.dept_id.unit_id.name, self.name)
