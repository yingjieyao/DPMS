#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from models import *

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'device_type', 'brand', 'date']

def listdevice(req):
    response = HttpResponse("hi")
    if req.method == 'GET':
        device = Device.objects.all()
        fm = list(device)
        return render_to_response('list_device.html', {'fm': fm}, context_instance=RequestContext(req))

def adddevice(req):
    response = HttpResponse("adddevice")
    if req.method == 'POST':
        fm = DeviceForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/listdevice/')
    else:
        fm = DeviceForm()
        return render_to_response('add_device.html', {'fm': fm}, context_instance=RequestContext(req))

def get_device_id(req):
    if req.method == 'GET':
        ids = req.GET.get('id')
        device = Device.objects.filter(pk = ids)
        print device[0]
        return render_to_response('device_update.html', {'data': device[0]}, context_instance=RequestContext(req))


def deletedevice(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        Device.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listdevice')

    return response
