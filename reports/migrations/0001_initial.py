# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataiumDMA'
        db.create_table(u'reports_dataiumdma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataiumdmaid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dmaname', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'reports', ['DataiumDMA'])

        # Adding model 'Dealer'
        db.create_table(u'reports_dealer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dealername', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('dealercity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dealerstate', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dealermainwebsite', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dma', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dma', to=orm['reports.DataiumDMA'])),
            ('dealerdma', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'reports', ['Dealer'])


    def backwards(self, orm):
        # Deleting model 'DataiumDMA'
        db.delete_table(u'reports_dataiumdma')

        # Deleting model 'Dealer'
        db.delete_table(u'reports_dealer')


    models = {
        u'reports.dataiumdma': {
            'Meta': {'object_name': 'DataiumDMA'},
            'dataiumdmaid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dmaname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.dealer': {
            'Meta': {'object_name': 'Dealer'},
            'dealercity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealerdma': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealermainwebsite': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealername': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dealerstate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dma': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dma'", 'to': u"orm['reports.DataiumDMA']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reports']