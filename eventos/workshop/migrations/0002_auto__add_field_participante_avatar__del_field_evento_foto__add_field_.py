# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Participante.avatar'
        db.add_column(u'workshop_participante', 'avatar',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Evento.foto'
        db.delete_column(u'workshop_evento', 'foto')

        # Adding field 'Evento.imagem'
        db.add_column(u'workshop_evento', 'imagem',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Participante.avatar'
        db.delete_column(u'workshop_participante', 'avatar')

        # Adding field 'Evento.foto'
        db.add_column(u'workshop_evento', 'foto',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Evento.imagem'
        db.delete_column(u'workshop_evento', 'imagem')


    models = {
        u'workshop.evento': {
            'Meta': {'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'workshop.palestra': {
            'Meta': {'object_name': 'Palestra'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workshop.Evento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_palestra': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'workshop.palestrante': {
            'Meta': {'object_name': 'Palestrante'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_palestrante': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'palestra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workshop.Palestra']"})
        },
        u'workshop.participante': {
            'Meta': {'object_name': 'Participante'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_participante': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'palestra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workshop.Palestra']"})
        }
    }

    complete_apps = ['workshop']