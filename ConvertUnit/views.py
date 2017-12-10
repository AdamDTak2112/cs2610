# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Convert
import json
# Create your views here.

def convert(value, to, fro):
    newValue = (value / Convert.factors[fro]) * Convert.factors[to]
    return newValue

def convertFromRequest(request):
    resp = {};
    if not request.GET.has_key('value' and 'from' and 'to'):
        resp['error'] = "Not a valid conversion factor"
    else:
        value = int(request.GET['value'])
        to = request.GET['to']
        fro = request.GET['from']
        if (value < 0):
            resp['error'] = "Not a valid number to convert"
        else:
           val = convert(value, to, fro)
           resp = { 'units': to, 'value': val }
           
    return HttpResponse(json.dumps(resp))
    
def index(request):
    return render(request, '')
            