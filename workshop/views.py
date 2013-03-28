# coding: utf-8

from django.shortcuts import render
from models import Evento

def index(request):
    """
    index for the site
    """
    valores = {'eventos': evento.objects.all()}
    return render(request, 'index.html', valores)
