#coding=utf8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import *
from user_mana_views import *
from device import *
from charge import *
from repair import *
from room import *
from complaint import *

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


def index(req):
    username = req.COOKIES.get('username', '')
    if not username:
        return render_to_response('reload_login.html', {'info': '请登陆', 'next': '登陆'}, context_instance=RequestContext(req))
    else:
        return render_to_response('index.html', {'username': username}, context_instance=RequestContext(req))

def login(req):
    username = req.COOKIES.get('username', '')
    if username:
        response = HttpResponseRedirect('/dpms/index/')
        response.set_cookie('username', username, 3600)
        return response

    if req.method == 'POST':
        user_form = UserForm(req.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = User_info.objects.filter(user_name__exact=username, password__exact=password)
            if user:
                response = HttpResponseRedirect('/dpms/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return render_to_response('reload_login.html', {'info': '用户名或密码错误', 'next': '登陆'}, context_instance=RequestContext(req))
    else:
        user_form = UserForm()
    return render_to_response('login.html', {'user_form': user_form}, context_instance=RequestContext(req))

def regist(req):
    if req.method == 'POST':
        user_form = UserForm(req.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            has = User_info.objects.filter(user_name=username)
            if has:
                return render_to_response('reload.html', {'info' : '用户名已存在', 'next': '登陆'}, context_instance=RequestContext(req))
            else:
                User_info.objects.create(user_name=username, password=password)
                response = HttpResponse('regist success!! <a href="/dpms/login/"> login </a>')
                response.set_cookie('username', username, 3600)
                return response
    else:
        user_form = UserForm()
    return render_to_response('regist.html', {'user_form': user_form}, context_instance=RequestContext(req))

def logout(req):
    response = HttpResponseRedirect("/dpms/login/")
    response.delete_cookie("username")
    return response

def change_password(req):
    if method == 'POST':
        user_name = req.POST['user_name']
        old = req.POST['old']
        new = req.POST['new']
        user = User_info.objects.filter(user_name=user_name, password=old)
        if len(user) == 0:
            return 'no exist'
        else:
            user.user_name = user_name
            user.password = new
            user.save()
            return HttpResponseRedirect('/dpms/index')
