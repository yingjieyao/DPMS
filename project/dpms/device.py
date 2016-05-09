#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q
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

def adddevice2(req):
    if req.method == "POST":
        data = Device()
        data.id = req.POST['id']
        data.name = req.POST['name']
        data.device_type = req.POST['device_type']
        data.brand = req.POST['brand']
        date = Device.objects.filter(pk = data.id)
        data.date = date[0].date

        # data.date = req.POST['date']
        data.save()
        return HttpResponseRedirect('/dpms/listdevice/')


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
        return render_to_response('device_update.html', {'data': device[0]}, context_instance=RequestContext(req))


def deletedevice(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        Device.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listdevice')

    return response

def get_device(req):
    if req.method == 'GET':
        typ = req.GET.get('type')
        f = Q()
        if len(typ):
            f = f & Q(('device_type', typ.strip()))
        device = Device.objects.filter(f)
        fm = list(device)
        return render_to_response('list_device.html', {'fm': fm}, context_instance=RequestContext(req))
    pass
