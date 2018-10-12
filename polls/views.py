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
    if request.is_ajax():
        if request.method == 'POST':
            data = request.POST.all()
            print
            data
            return HttpResponse( json.dumps( {'data': data} ), content_type="application/json" )
    else:
        print
        "you are not in ajax"
        return render( 'poll/ajax_test.html', locals() )


def ajax_test(request):
    if request.is_ajax():
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)
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

