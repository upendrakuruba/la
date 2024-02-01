from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def first(request):
    return HttpResponse ('this is a app project')