from django.conf.urls import url

from . import views

app_name = "puncher"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<checkpoint_id>[0-9]+)/punch/$', views.punch, name='punch'),
    url(r'^(?P<checkpoint_id>[0-9]+)/accepted/$', views.accepted, name='accepted'),
]
