from django.conf.urls import url
from django.contrib import admin

from dpms import views

urlpatterns = [
        url(r'^$', views.login, name='login'),
        url(r'^login/$', views.login, name='login'),
        url(r'^regist/$', views.regist, name='regist'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^index/$', views.index, name='index'),
]
