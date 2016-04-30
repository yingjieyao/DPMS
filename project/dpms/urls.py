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
        url(r'^alteruser/$', views.alteruser, name='alteruser'),
        url(r'^deleteuser/$', views.deleteuser, name='deleteuser'),
        url(r'^listdevice/$', views.listdevice, name='listdevice'),
]
