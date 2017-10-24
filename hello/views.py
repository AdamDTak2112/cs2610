from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def index(request):
	return HttpResponse("The time over here is: " + time.strftime("%c"))