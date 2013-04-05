# coding: utf-8

from django.shortcuts import render
from models import Event, Palestra


def index(request):
    """
    index for the site
    """
    context = {'eventos': Evento.objects.order_by('data')}
    return render(request, 'index.html', context)
