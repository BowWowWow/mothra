# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dealer.dealerlat'
        db.add_column(u'reports_dealer', 'dealerlat',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6),
                      keep_default=False)

        # Adding field 'Dealer.dealerlong'
        db.add_column(u'reports_dealer', 'dealerlong',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Dealer.dealerlat'
        db.delete_column(u'reports_dealer', 'dealerlat')

        # Deleting field 'Dealer.dealerlong'
        db.delete_column(u'reports_dealer', 'dealerlong')


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
            'dealerlat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6'}),
            'dealerlong': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6'}),
            'dealermainwebsite': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealername': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dealerstate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dma': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dma'", 'to': u"orm['reports.DataiumDMA']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reports']