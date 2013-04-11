# coding: utf-8

from django.contrib import admin
from eventos.workshop.models import Evento, Palestrante, Palestra, \
    Participante


class EventoAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'descricao']
    list_filter = ['data']


class PalestranteAdmin(admin.ModelAdmin):
    search_fields = ['nome_palestrante']


class PalestraAdmin(admin.ModelAdmin):
    search_fields = ['nome_palestra']


class Participante(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Evento, EventoAdmin)
admin.site.register(Palestrante, PalestranteAdmin)
admin.site.register(Palestra, PalestraAdmin)
admin.site.register(Participante, ParticipanteAdmin)
