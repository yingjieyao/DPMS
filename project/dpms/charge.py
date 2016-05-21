#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from django.db.models import Q
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
        for ch in charge:
            print ch.user_id
        fm = list(charge)
        return render_to_response('list_charge_main.html', {'fm': fm}, context_instance=RequestContext(req))

def addcharge2(req):
    if req.method == "POST":
        data = Charge()
        data.id = req.POST['id']
        data.user_id = User_info.objects.filter(pk = req.POST['user_id'])[0]
        date = Charge.objects.filter(pk = data.id)
        data.charge_date = date[0].charge_date
        data.charge_type = req.POST['charge_type']
        data.charge_date = req.POST['charge_date']
        data.charge_total = req.POST['charge_total']
        data.charge_complet = req.POST['charge_complet']
        data.charge_cont = req.POST['charge_cont']
        data.save()
        return HttpResponseRedirect('/dpms/listcharge/')



def addcharge(req):
    if req.method == 'POST':
        fm = ChargeForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/listcharge/')
    else:
        fm = ChargeForm()
        return render_to_response('add_charge_main.html', {'fm': fm}, context_instance=RequestContext(req))

def get_charge_id(req):
    if req.method == 'GET':
        ids = req.GET.get('id')
        device = Charge.objects.filter(pk = ids)
        return render_to_response('charge_update_main.html', {'data': device[0]}, context_instance=RequestContext(req))


def deletecharge(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        Charge.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listcharge')

    return response

def get_charge(req):
    if req.method == "GET":
        name = req.GET.get("name")
        f = Q()
        if len(name):
            f = f & Q(('user_name', name.strip()))
            users = User_info.objects.filter(f)
            if len(users) == 0:
                fm = []
                return render_to_response('list_charge.html', {'fm': fm}, context_instance=RequestContext(req))
            else:
                t = Q()
                t = t & Q(("user_id", users[0].id))
                lis = Charge.objects.filter(t)
                fm = list(lis)
                return render_to_response('list_charge_main.html', {'fm': fm}, context_instance=RequestContext(req))
        else:
            return HttpResponseRedirect("/dpms/listcharge/")

