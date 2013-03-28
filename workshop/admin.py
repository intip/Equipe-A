from django.contrib import admin
from  workshop.models import Evento, Palestrante, Palestra,\
                                                    Participante

admin.site.register(Evento)
admin.site.register(Palestrante)
admin.site.register(Palestra)
admin.site.register(Participante)
