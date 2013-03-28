# coding: utf-8

from django.shortcuts import render
from models import Evento

def index(request, context={}):
    """
    index for the site
    """
    context = {'eventos': Evento.objects.all()}
    return render(request, 'index.html', context)

def evento(request):
    pass
