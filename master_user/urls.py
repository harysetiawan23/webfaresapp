from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.login_user, name='login'),
    url(r'^register_user', views.register_user, name='register_user'),
    url(r'^delete_user$', views.delete_user, name='delete_user'),
    url(r'^update_user', views.upadate_user, name='update_user'),
]
