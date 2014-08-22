# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DealerMarketReport.marketreportinactive'
        db.add_column(u'reports_dealermarketreport', 'marketreportinactive',
                      self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True),
                      keep_default=False)

        # Adding field 'DealerMarketReport.marketreportdeleted'
        db.add_column(u'reports_dealermarketreport', 'marketreportdeleted',
                      self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True),
                      keep_default=False)

        # Adding field 'DealerMarketReport.marketreportcreatedate'
        db.add_column(u'reports_dealermarketreport', 'marketreportcreatedate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DealerMarketReport.marketreportupdatedate'
        db.add_column(u'reports_dealermarketreport', 'marketreportupdatedate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DealerMarketReport.marketreportinactive'
        db.delete_column(u'reports_dealermarketreport', 'marketreportinactive')

        # Deleting field 'DealerMarketReport.marketreportdeleted'
        db.delete_column(u'reports_dealermarketreport', 'marketreportdeleted')

        # Deleting field 'DealerMarketReport.marketreportcreatedate'
        db.delete_column(u'reports_dealermarketreport', 'marketreportcreatedate')

        # Deleting field 'DealerMarketReport.marketreportupdatedate'
        db.delete_column(u'reports_dealermarketreport', 'marketreportupdatedate')


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
        u'reports.dealermarketreport': {
            'Meta': {'object_name': 'DealerMarketReport'},
            'dealer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Dealer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketreportasiimage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'marketreportcreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'marketreportdeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'marketreportdescr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marketreportdmmimage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'marketreportinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'marketreportmessage': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marketreportmiscimage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'marketreportnotes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marketreportshopimage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'marketreportsocialimage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'marketreportupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'marketreportutilityimage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reportyearmonth': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.MarketReportYearMonth']"})
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
            'marketreportyearmonthchar': ('django.db.models.fields.CharField', [], {'max_length': '6', 'unique': 'True', 'null': 'True'}),
            'marketreportyearmonthcreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'marketreportyearmonthdeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'marketreportyearmonthinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'marketreportyearmonthupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reports']