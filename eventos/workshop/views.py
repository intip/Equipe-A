# coding: utf-8

from django.shortcuts import render
from models import Evento, Palestra


def index(request, context={}):
    """
    index for the site
    """
    context = {'eventos': Evento.objects.order_by('data')}
    return render(request, 'index.html', context)
