# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'workshop_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'workshop', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'workshop_contact')


    models = {
        u'workshop.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
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