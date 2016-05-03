from django.conf.urls import url
from django.contrib import admin

from dpms import views

urlpatterns = [
        url(r'^$', views.login, name='login'),
        url(r'^login/$', views.login, name='login'),
        url(r'^regist/$', views.regist, name='regist'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^index/$', views.index, name='index'),
        url(r'^listuser/$', views.listuser, name='listuser'),
        url(r'^adduser/$', views.adduser, name='adduser'),
        url(r'^adduser2/$', views.adduser2, name='adduser2'),
        url(r'^alteruser/$', views.alteruser, name='alteruser'),
        url(r'^deleteuser/$', views.deleteuser, name='deleteuser'),
        url(r'^listdevice/$', views.listdevice, name='listdevice'),
        url(r'^adddevice/$', views.adddevice, name='adddevice'),
        url(r'^adddevice2/$', views.adddevice2, name='adddevice2'),
        url(r'^deletedevice/$', views.deletedevice, name='deldevice'),
        url(r'^getdevice/$', views.get_device_id, name='device_id'),
]
