from django.shortcuts import render
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    template = loader.get_template('base_Home.html')
    return HttpResponse(template.render({}, request))