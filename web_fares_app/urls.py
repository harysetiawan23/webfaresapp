
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^master/', include('master_asset.urls')),
    url(r'^jadwal/',include('master_jadwal.urls')),
    url(r'^control/',include('master_scheduling.urls')),
    url(r'^user/',include('master_user.urls')),

    # url(r'^login', views.login),
    # url(r'^test',views.simpleData),
    url(r'^$', views.index,name='index'),
    url(r'^logout',views.signout,name='logout'),

    url(r'^systemStat',views.systemStat,name='sysstat')
]
