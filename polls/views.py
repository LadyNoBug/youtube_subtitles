from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ../youtube-transcript-api import *


def index(request):
    str = 'haha'
    return HttpResponse(str)