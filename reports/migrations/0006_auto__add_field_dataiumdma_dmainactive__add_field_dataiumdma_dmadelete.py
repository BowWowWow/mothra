# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DataiumDMA.dmainactive'
        db.add_column(u'reports_dataiumdma', 'dmainactive',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Adding field 'DataiumDMA.dmadeleted'
        db.add_column(u'reports_dataiumdma', 'dmadeleted',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Adding field 'DataiumDMA.dmacreatedate'
        db.add_column(u'reports_dataiumdma', 'dmacreatedate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DataiumDMA.dmaupdatedate'
        db.add_column(u'reports_dataiumdma', 'dmaupdatedate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Dealer.dealeractive'
        db.delete_column(u'reports_dealer', 'dealeractive')

        # Adding field 'Dealer.dealerinactive'
        db.add_column(u'reports_dealer', 'dealerinactive',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Adding field 'Dealer.dealercreatedate'
        db.add_column(u'reports_dealer', 'dealercreatedate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dealer.dealerupdatedate'
        db.add_column(u'reports_dealer', 'dealerupdatedate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DataiumDMA.dmainactive'
        db.delete_column(u'reports_dataiumdma', 'dmainactive')

        # Deleting field 'DataiumDMA.dmadeleted'
        db.delete_column(u'reports_dataiumdma', 'dmadeleted')

        # Deleting field 'DataiumDMA.dmacreatedate'
        db.delete_column(u'reports_dataiumdma', 'dmacreatedate')

        # Deleting field 'DataiumDMA.dmaupdatedate'
        db.delete_column(u'reports_dataiumdma', 'dmaupdatedate')

        # Adding field 'Dealer.dealeractive'
        db.add_column(u'reports_dealer', 'dealeractive',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True),
                      keep_default=False)

        # Deleting field 'Dealer.dealerinactive'
        db.delete_column(u'reports_dealer', 'dealerinactive')

        # Deleting field 'Dealer.dealercreatedate'
        db.delete_column(u'reports_dealer', 'dealercreatedate')

        # Deleting field 'Dealer.dealerupdatedate'
        db.delete_column(u'reports_dealer', 'dealerupdatedate')


    models = {
        u'reports.dataiumdma': {
            'Meta': {'object_name': 'DataiumDMA'},
            'dataiumdmaid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dmacreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dmadeleted': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'dmainactive': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'dmaname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dmaupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.dealer': {
            'Meta': {'object_name': 'Dealer'},
            'dealercity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealercreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dealerdeleted': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'dealerdma': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealerinactive': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'dealerlat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6'}),
            'dealerlong': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6'}),
            'dealermainwebsite': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealername': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dealerstate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dealerupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'dma': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'DMA'", 'to': u"orm['reports.DataiumDMA']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reports']