# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MarketReportYearMonth'
        db.create_table(u'reports_marketreportyearmonth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marketreportyearmonthchar', self.gf('django.db.models.fields.CharField')(default=0, max_length=6, null=True)),
            ('marketreportyearmonthdesc', self.gf('django.db.models.fields.CharField')(default=0, max_length=16, null=True)),
            ('marketreportyearmonthinactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('marketreportyearmonthdeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('marketreportyearmonthcreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('marketreportyearmonthupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['MarketReportYearMonth'])


    def backwards(self, orm):
        # Deleting model 'MarketReportYearMonth'
        db.delete_table(u'reports_marketreportyearmonth')


    models = {
        u'reports.dataiumdma': {
            'Meta': {'object_name': 'DataiumDMA'},
            'dataiumdmaid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dmacreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dmadeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'dmainactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'dmaname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dmaupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.dealer': {
            'Meta': {'object_name': 'Dealer'},
            'dealercity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealercreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dealerdeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'dealerdma': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealerinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'dealerlat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6'}),
            'dealerlong': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6'}),
            'dealermainwebsite': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dealername': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dealerstate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dealerupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'dma': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'DMA'", 'to': u"orm['reports.DataiumDMA']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.dealersite': {
            'Meta': {'object_name': 'DealerSite'},
            'dataiumsitedescription': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'dataiumsiteid': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'dealer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Dealer']"}),
            'dealersitecreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dealersitedeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'dealersiteinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'dealersiteupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.marketreportyearmonth': {
            'Meta': {'object_name': 'MarketReportYearMonth'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketreportyearmonthchar': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '6', 'null': 'True'}),
            'marketreportyearmonthcreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'marketreportyearmonthdeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'marketreportyearmonthdesc': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '16', 'null': 'True'}),
            'marketreportyearmonthinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'marketreportyearmonthupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reports']