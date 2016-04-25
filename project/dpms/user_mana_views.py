#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from models import *

class UserInfoForm(ModelForm):
    class Meta:
        model = User_info
        fields = ['user_name', 'user_gender', 'user_hometown', 'user_phone',
                'user_idcard', 'user_company']

def listuser(req):
    response = HttpResponse("hi")
    if req.method == 'GET':
        all_users = User_info.objects.all()
        fm = list(all_users)
        return render_to_response('list_user.html', {'fm': fm}, context_instance=RequestContext(req))

def adduser(req):
    response = HttpResponse("adduser")
    if req.method == 'POST':
        fm = UserInfoForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/listuser/')
    else:
        fm = UserInfoForm()
        return render_to_response('add_user.html', {'fm': fm}, context_instance=RequestContext(req))

def alteruser(req):
    response = HttpResponse("alteruser")
    return response

def deleteuser(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        User_info.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listuser')

    response = HttpResponse("deleteuser")
    return response
