# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Evento'
        db.create_table(u'workshop_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'workshop', ['Evento'])

        # Adding model 'Palestra'
        db.create_table(u'workshop_palestra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_palestra', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workshop.Evento'])),
        ))
        db.send_create_signal(u'workshop', ['Palestra'])

        # Adding model 'Participante'
        db.create_table(u'workshop_participante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_participante', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('palestra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workshop.Palestra'])),
        ))
        db.send_create_signal(u'workshop', ['Participante'])

        # Adding model 'Palestrante'
        db.create_table(u'workshop_palestrante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_palestrante', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('palestra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workshop.Palestra'])),
        ))
        db.send_create_signal(u'workshop', ['Palestrante'])


    def backwards(self, orm):
        # Deleting model 'Evento'
        db.delete_table(u'workshop_evento')

        # Deleting model 'Palestra'
        db.delete_table(u'workshop_palestra')

        # Deleting model 'Participante'
        db.delete_table(u'workshop_participante')

        # Deleting model 'Palestrante'
        db.delete_table(u'workshop_palestrante')


    models = {
        u'workshop.evento': {
            'Meta': {'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_participante': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'palestra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workshop.Palestra']"})
        }
    }

    complete_apps = ['workshop']