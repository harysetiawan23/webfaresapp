from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^schedule', views.scheduleClass, name='schedule'),
    url(r'^kelas-pelajar', views.studentClass,name='kelas-pelajar'),
]
