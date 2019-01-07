from django.conf.urls import url
from .views import controlStudentClass

urlpatterns = [
    url(r'^kelas', controlStudentClass.scheduleClass, name='kelas'),
    url(r'^pelajar$', controlStudentClass.studentClass, name='kelas-pelajar'),

    url(r'^store-pelajar-kelas', controlStudentClass.storePelajarKelas, name='store-pelajar-kelas'),
    url(r'^drop-pelajar-kelas$', controlStudentClass.dropPelajarKelas, name='drop-pelajar-kelas'),
]
