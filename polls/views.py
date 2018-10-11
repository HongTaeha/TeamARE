# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import polls
import requests
from django.http import HttpResponse
from Lawdcd.models import Lawdcd
import json
# Create your views here.


def introduce_tables(request):
    lawdcd=Lawdcd.objects.all()
    context={'Lawdcd': lawdcd}    
    return render(request, 'introduce/tables.html',context)

def introduce_index(request):
    lawdcd=Lawdcd.objects.all()
    context={'Lawdcd': lawdcd}    
    return render(request, 'introduce/index.html',context)

def data(request):
    if request.method =='POST':
        request_data = ((request.body).decode('utf-8'))
        request_data = json.loads(request_data)
        content = request_data['content']

    return HttpResponse(content)


def introduce_login(request):
	return render(request, 'introduce/login.html',{})

def introduce_register(request):
	return render(request, 'introduce/register.html',{})

def introduce_blank(request):
	return render(request, 'introduce/blank.html',{})

def introduce_charts(request):
    lawdcd=Lawdcd.objects.all()
    context={'Lawdcd': lawdcd}    
    return render(request, 'introduce/charts.html',context)


def introduce_study(request):
	return render(request, 'introduce/study_lee.html',{})

