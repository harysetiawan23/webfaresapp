from django.contrib import admin

# Register your models here.
from .models import  student, classRoom, subject, shift, teacher, \
    teacherFace, departement, religion, unit,  studentFace


admin.site.register(student)
admin.site.register(classRoom)
admin.site.register(subject)
admin.site.register(shift)
admin.site.register(teacherFace)
admin.site.register(teacher)
admin.site.register(departement)
admin.site.register(religion)
admin.site.register(unit)
admin.site.register(studentFace)

