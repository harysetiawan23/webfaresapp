from django.conf.urls import url
from .views import controlStudentClass

urlpatterns = [
    url(r'^kelas', controlStudentClass.scheduleClass, name='kelas'),
    url(r'^pelajar$', controlStudentClass.studentClass,name='kelas-pelajar'),
]
