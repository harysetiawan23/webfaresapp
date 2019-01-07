from django.conf.urls import url
from . import views

from .views import controlJamPelajaran, controlShiftKelas, controlTeamTeaching, controlSubjectOffer

urlpatterns = [

    url(r'^team-teaching', controlTeamTeaching.masterTeamTeaching, name='team-teaching'),
    url(r'^store-teaching', controlTeamTeaching.storeTeamTeaching, name='store-teaching'),
    url(r'^update-teaching', controlTeamTeaching.updateTeamTeaching, name='update-teaching'),
    url(r'^drop-teaching$', controlTeamTeaching.dropTeamTeaching, name='drop-teaching'),

    url(r'^teaching',controlTeamTeaching.dtTeamTeaching,name='dt-team-teaching'),
    url(r'^store-teacher-team-teaching', controlTeamTeaching.storeTeacherTeamTeaching, name='store-teacher-team'),
    url(r'^drop-teacher-team-teaching$', controlTeamTeaching.dropTeacherTeamTeaching, name='drop-teacher-team'),

    url(r'^jenis-kelas', controlShiftKelas.masterJenisKelas, name='jenis-kelas'),
    url(r'^store-kelas', controlShiftKelas.storeJenisKelas, name='store-kelas'),
    url(r'^update-kelas', controlShiftKelas.updateJenisKelas, name='update-kelas'),
    url(r'^drop-kelas$', controlShiftKelas.dropJenisKelas, name='drop-kelas'),

    url(r'^penawaran', controlSubjectOffer.masterSubjectOffer, name='penawaran-mata-pelajaran'),
    url(r'^store-penawaran', controlSubjectOffer.storeSubjectOffer, name='store-penawaran'),
    url(r'^update-penawaran', controlSubjectOffer.updateSubjectOffer, name='update-penawaran'),
    url(r'^drop-penawaran$', controlSubjectOffer.dropSubjectOffer, name='drop-penawaran'),

    url(r'^jam', controlJamPelajaran.masterJamPelajaran, name='jam-pelajaran'),
    url(r'^store-jam', controlJamPelajaran.storejamPelajaran, name='store-jam'),
    url(r'^update-jam', controlJamPelajaran.updatejamPelajaran, name='update-jam'),
    url(r'^drop-jam$', controlJamPelajaran.dropjamPelajaran, name='drop-jam')
]
