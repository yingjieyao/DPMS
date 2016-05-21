#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q
from django import forms
from django.forms import ModelForm
from models import *

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['user_id', 'comp_date', 'comp_content']

def listcomplaint(req):
    response = HttpResponse("hi")
    if req.method == 'GET':
        complaint = Complaint.objects.all()
        fm = list(complaint)
        return render_to_response('list_comp_main.html', {'fm': fm}, context_instance=RequestContext(req))

def addcomplaint2(req):
    if req.method == "POST":
        data = Complaint()
        data.id = req.POST['id']
        data.user_id = req.POST['user_id']
        # data.comp_date = req.POST['comp_date']
        data.comp_content = req.POST['comp_content']
        date = Complaint.objects.filter(pk = data.id)
        data.date = date[0].date

        # data.date = req.POST['date']
        data.save()
        return HttpResponseRedirect('/dpms/listcomplaint/')


def addcomplaint(req):
    if req.method == 'POST':
        fm = ComplaintForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/listcomplaint/')
    else:
        fm = ComplaintForm()
        return render_to_response('add_complaint.html', {'fm': fm}, context_instance=RequestContext(req))

def get_complaint_id(req):
    if req.method == 'GET':
        ids = req.GET.get('id')
        device = Complaint.objects.filter(pk = ids)
        return render_to_response('complaint_update.html', {'data': device[0]}, context_instance=RequestContext(req))


def deletecomplaint(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        Complaint.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listcomplaint')

    return response

def get_complaint(req):
    pass
    # if req.method == 'GET':
    #     typ = req.GET.get('type')
    #     f = Q()
    #     if len(typ):
    #         f = f & Q(('device_type', typ.strip()))
    #     device = Device.objects.filter(f)
    #     fm = list(device)
    #     return render_to_response('list_device.html', {'fm': fm}, context_instance=RequestContext(req))
