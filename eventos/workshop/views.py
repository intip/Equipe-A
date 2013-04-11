# coding: utf-8

from django.shortcuts import render
from models import Evento, Palestra
from forms import ContactForm

def index(request, context={}):
    """
    index for the site
    """

    context = {'eventos': Evento.objects.order_by('data')}
    return render(request, 'index.html', context)

def data(request, context={}):

    context = {'eventos': Evento.objects.order_by('data')}
    return render(request, 'index.html', context)

def titulo(request, context={}):

    context = {'eventos': Evento.objects.order_by('titulo')}
    return render(request, 'index.html', context)

def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        raise
