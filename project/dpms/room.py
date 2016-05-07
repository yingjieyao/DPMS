#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['building_id', 'room_name', 'room_size', 'user_id']

def listroom(req):
    response = HttpResponse("hi")
    if req.method == 'GET':
        room = Room.objects.all()
        fm = list(room)
        return render_to_response('list_room.html', {'fm': fm}, context_instance=RequestContext(req))

def addroom2(req):
    if req.method == "POST":
        data = Room()
        data.id = req.POST['id']
        data.user_id = User_info.objects.filter(pk = req.POST['user_id'])[0]
        data.building_id= req.POST['building_id']
        data.room_name = req.POST['room_name']
        data.room_size = req.POST['room_size']
        data.save()
        return HttpResponseRedirect('/dpms/listroom/')



def addroom(req):
    if req.method == 'POST':
        fm = RoomForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/listroom/')
    else:
        fm = RoomForm()
        return render_to_response('add_room.html', {'fm': fm}, context_instance=RequestContext(req))

def get_room_id(req):
    if req.method == 'GET':
        ids = req.GET.get('id')
        device = Room.objects.filter(pk = ids)
        return render_to_response('room_update.html', {'data': device[0]}, context_instance=RequestContext(req))


def deleteroom(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        print 'room id', id
        Room.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listroom')

    return response
