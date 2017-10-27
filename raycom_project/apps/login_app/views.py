# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User
from django.contrib import messages
from django.shortcuts import render, redirect
import datetime

def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    errors = User.objects.registerVal(request.POST)
    if len(errors) != 0:
        for error in errors.itervalues():
            messages.error(request, error)
    else:
        User.objects.createUser(request.POST)
        messages.success(request, "User created")
    return redirect('/')

def login(request):
    results = User.objects.loginUser(request.POST)
    if type(results) == dict:
        for error in results.itervalues():
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['first_name']=results.first_name
        request.session['last_name']=results.last_name
        request.session['email']=results.email
        request.session['id']=results.id
        return redirect('/home')

def logout(request):
    request.session.flush()
    return redirect('/')

# Type localhost:8000/clear to reset Userdata

def clear(request):
    User.objects.all().delete()
    return redirect('/')
        

