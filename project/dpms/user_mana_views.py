#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.db.models import Q
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

def adduser2(req):
    response = HttpResponse("adduser")
    if req.method == 'POST':
        fm = UserInfoForm(req.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/dpms/listuser/')
    else:
        fm = UserInfoForm()
        return render_to_response('add_user.html', {'fm': fm}, context_instance=RequestContext(req))


def adduser(req):
    response = HttpResponse("adduser")
    if req.method == 'POST':
        fm = UserInfoForm(req.POST)
        user = User_info()
        data = req.POST
        id = req.POST['id']
        if len(id) > 0:
            user.id = data['id']
        user.user_name = data['user_name']
        user.user_hometown = data['user_hometown']
        user.user_phone = data['user_phone']
        user.user_idcard = data['user_idcard']
        user.user_company = data['user_company']
        user.save()
        # if fm.is_valid():
        #     fm.save()
        return HttpResponseRedirect('/dpms/listuser/')
    else:
        fm = UserInfoForm()
        return render_to_response('add_user.html', {'fm': fm}, context_instance=RequestContext(req))

def alteruser(req):
    if req.method == 'GET':
        ids = req.GET.get('id')
        user = User_info.objects.filter(pk = ids)
        return render_to_response('user_update.html', {'data': user[0]}, context_instance=RequestContext(req))

def deleteuser(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        User_info.objects.filter(pk=req.GET.get('id')).delete()
        return HttpResponseRedirect('/dpms/listuser')

    response = HttpResponse("deleteuser")
    return response

def get_user(req):
    if req.method == 'GET':
        name = req.GET.get('name')
        idnumber = req.GET.get('idnumber')
        f = Q()
        if len(name):
            f = f & Q(('user_name', name.strip()))

        if len(idnumber):
            f = f & Q(('user_idcard', idnumber.strip()))

        user = User_info.objects.filter(f)
        fm = list(user)
        return render_to_response('list_user.html', {'fm': fm}, context_instance=RequestContext(req))
