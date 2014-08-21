# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        from django.core.management import call_command
        call_command("loaddata","reports_sampledata.json")
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
