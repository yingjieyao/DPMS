#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from models import *

class ChargeForm(ModelForm):
    class Meta:
        model = Charge
        fields = ['user_id', 'charge_date', 'charge_type', 'charge_total',
                'charge_complet', 'charge_cont']

def listcharge(req):
    response = HttpResponse("hi")
    if req.method == 'GET':
        charge = Charge.objects.all()
        fm = list(charge)
        return render_to_response('list_charge.html', {'fm': fm}, context_instance=RequestContext(req))

def addcharge2(req):
    if req.method == "POST":
        data = Charge()
        data.id = req.POST['id']
        data.user_id = req.POST['user_id']
        date = Device.objects.filter(pk = data.id)
        data.date = date[0].date

        # data.date = req.POST['date']
        data.save()
        return HttpResponseRedirect('/dpms/listcharge/')



def addcharge(req):
    response = HttpResponse("adddevice")
    if req.method == 'POST':
        fm = ChargeForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/listcharge/')
    else:
        fm = ChargeForm()
        return render_to_response('add_charge.html', {'fm': fm}, context_instance=RequestContext(req))

def get_charge_id(req):
    if req.method == 'GET':
        ids = req.GET.get('id')
        device = Charge.objects.filter(pk = ids)
        return render_to_response('charge_update.html', {'data': device[0]}, context_instance=RequestContext(req))


def deletecharge(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        Charge.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listcharge')

    return response
