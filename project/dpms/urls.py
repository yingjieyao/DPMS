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
        url(r'^listuser2/$', views.listuser2, name='listuser'),
        url(r'^adduser/$', views.adduser, name='adduser'),
        url(r'^adduser_self/$', views.adduser_self, name='adduser_self'),
        url(r'^adduser2/$', views.adduser2, name='adduser2'),
        url(r'^alteruser/$', views.alteruser, name='alteruser'),
        url(r'^alteruserbyname/$', views.alteruserbyname, name='alteruserbyname'),
        url(r'^deleteuser/$', views.deleteuser, name='deleteuser'),
        url(r'^get_user/$', views.get_user, name='get_user'),
        url(r'^change_pass/$', views.change_password, name='change_pass'),
        url(r'^change_profile/$', views.change_profile, name='change_profile'),

        url(r'^listdevice/$', views.listdevice, name='listdevice'),
        url(r'^adddevice/$', views.adddevice, name='adddevice'),
        url(r'^adddevice2/$', views.adddevice2, name='adddevice2'),
        url(r'^deletedevice/$', views.deletedevice, name='deldevice'),
        url(r'^get_device_id/$', views.get_device_id, name='device_id'),
        url(r'^get_device/$', views.get_device, name='device'),

        url(r'^get_charge_id/$', views.get_charge_id, name='charge_id'),
        url(r'^get_charge/$', views.get_charge, name='charge'),
        url(r'^addcharge/$', views.addcharge, name='addcharge'),
        url(r'^addcharge2/$', views.addcharge2, name='addcharge2'),
        url(r'^listcharge/$', views.listcharge, name='listcharge'),
        url(r'^deletecharge/$', views.deletecharge, name='deletecharge'),

        url(r'^get_repair_id/$', views.get_repair_id, name='repair_id'),
        url(r'^addrepair/$', views.addrepair, name='addrepair'),
        url(r'^addrepair2/$', views.addrepair2, name='addrepair2'),
        url(r'^listrepair/$', views.listrepair, name='listrepair'),
        url(r'^deleterepair/$', views.deleterepair, name='deleterepair'),

        url(r'^get_room/$', views.get_room, name='room'),
        url(r'^get_room_id/$', views.get_room_id, name='room_id'),
        url(r'^addroom/$', views.addroom, name='addroom'),
        url(r'^addroom2/$', views.addroom2, name='addroom2'),
        url(r'^listroom/$', views.listroom, name='listroom'),
        url(r'^deleteroom/$', views.deleteroom, name='deleteroom'),

        url(r'^get_complaint/$', views.get_complaint, name='complaint'),
        url(r'^get_complaint_id/$', views.get_complaint_id, name='complaint_id'),
        url(r'^addcomplaint/$', views.addcomplaint, name='addcomplaint'),
        url(r'^addcomplaint2/$', views.addcomplaint2, name='addcomplaint2'),
        url(r'^listcomplaint/$', views.listcomplaint, name='listcomplaint'),
        url(r'^deletecomplaint/$', views.deletecomplaint, name='deletecomplaint'),
]
