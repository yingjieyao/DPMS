#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from models import *

class RepairForm(ModelForm):
    class Meta:
        model = Repair
        fields = ['user_id', 'repair_date', 'repair_content']

def listrepair(req):
    response = HttpResponse("hi")
    if req.method == 'GET':
        charge = Repair.objects.all()
        fm = list(charge)
        return render_to_response('list_repair_main.html', {'fm': fm}, context_instance=RequestContext(req))

def addrepair2(req):
    if req.method == "POST":
        data = Repair()
        data.id = req.POST['id']
        data.user_id = User_info.objects.filter(pk = req.POST['user_id'])[0]
        data.repair_date = req.POST['repair_date']
        data.repair_content = req.POST['repair_content']
        # date = Device.objects.filter(pk = data.id)
        # data.date = date[0].date

        # data.date = req.POST['date']
        data.save()
        return HttpResponseRedirect('/dpms/listrepair/')

def addrepair(req):
    response = HttpResponse("adddevice")
    if req.method == 'POST':
        fm = RepairForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/index/')
    else:
        fm = RepairForm()
        if req.COOKIES.get('username', '') == 'root':
            return render_to_response('add_repair_main.html', {'fm': fm}, context_instance=RequestContext(req))
        else:
            return render_to_response('add_repair_main_user.html', {'fm': fm}, context_instance=RequestContext(req))

def get_repair_id(req):
    if req.method == 'GET':
        ids = req.GET.get('id')
        device = Repair.objects.filter(pk = ids)
        return render_to_response('repair_update.html', {'data': device[0]}, context_instance=RequestContext(req))


def deleterepair(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        Repair.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listrepair')

    return response
