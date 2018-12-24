from django.conf.urls import url

from .views import controlRuang, controlPelajaran, controlPelajar, controlPengajar,master_user

urlpatterns = [
    url(r'^pelajar/', controlPelajar.master_pelajar, name='master-pelajar'),

    url(r'^pelajaran/', controlPelajaran.master_pelajaran, name='master-pelajaran'),
    url(r'^store-pelajaran', controlPelajaran.tambahPelajaran, name='store-pelajaran'),
    url(r'^update-pelajaran', controlPelajaran.ubahPelajaran, name='update-pelajaran'),
    url(r'^drop-pelajaran$', controlPelajaran.hapusPelajaran, name='drop-pelajaran'),

    url(r'^pengajar/', controlPengajar.master_pengajar, name='master-pengajar'),
    url(r'^store-pengajar', controlPengajar.tambahPengajar, name='store-pengajar'),
    url(r'^update-pengajar', controlPengajar.updatePengajar, name='update-pengajar'),
    url(r'^drop-pengajar$', controlPengajar.dropPengajar, name='drop-pengajar'),

    url(r'^ruang/', controlRuang.master_ruang, name='master-ruang'),
    url(r'^store-ruang', controlRuang.storeRuang, name='store-ruang'),
    url(r'^update-ruang', controlRuang.updateRuang, name='update-ruang'),
    url(r'^drop-ruang$', controlRuang.dropRuang, name='drop-ruang'),

    url(r'^user/', master_user, name='master-user'),

]
