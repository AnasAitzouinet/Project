from django.shortcuts import render
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    template = loader.get_template('base_home.html')
    return HttpResponse(template.render({}, request))
def home(request):
    template = loader.get_template('Home/index.html')
    return HttpResponse(template.render({},request))
def reserve(request):
    template = loader.get_template('reservations/reserver.html')
    return HttpResponse(template.render({},request))
def Excursion(request):
    template = loader.get_template('Excursion/excursion.html')
    return HttpResponse(template.render({},request))