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
            ('dmainactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('dmadeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('dmacreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('dmaupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['DataiumDMA'])

        # Adding model 'DealerGroup'
        db.create_table(u'reports_dealergroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dealergroupname', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('dealergroupcity', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dealergroupstate', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dealergrouptype', self.gf('django.db.models.fields.CharField')(default='Auto Group', max_length=30, null=True, blank=True)),
            ('dealergroupcontactname', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('dataiumclientid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dealergroupinactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True, blank=True)),
            ('dealergroupdeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True, blank=True)),
            ('dealergroupcreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('dealergroupupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['DealerGroup'])

        # Adding model 'Dealer'
        db.create_table(u'reports_dealer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dealername', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('dealercity', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dealerstate', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dealermainwebsite', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dma', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='DMA', null=True, to=orm['reports.DataiumDMA'])),
            ('dealergroup', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Dealer Group', null=True, to=orm['reports.DealerGroup'])),
            ('dataiumsiteid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dealerdma', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dealerlat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('dealerlong', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('dealerinactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True, blank=True)),
            ('dealerdeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('dealercreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('dealerupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Dealer'])

        # Adding model 'DealerSite'
        db.create_table(u'reports_dealersite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dealer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Dealer'])),
            ('dataiumsiteid', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('dataiumsitedescription', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('dealersiteinactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('dealersitedeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('dealersitecreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('dealersiteupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['DealerSite'])

        # Adding model 'MarketReportYearMonth'
        db.create_table(u'reports_marketreportyearmonth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marketreportyearmonthchar', self.gf('django.db.models.fields.CharField')(max_length=6, unique=True, null=True)),
            ('marketreportyearmonthinactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('marketreportyearmonthdeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('marketreportyearmonthcreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('marketreportyearmonthupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['MarketReportYearMonth'])

        # Adding model 'UserProfile'
        db.create_table(u'reports_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('dealer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Dealer'], null=True, blank=True)),
            ('dealergroup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.DealerGroup'], null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('has_optedout', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wants_alerts', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wants_marketinfo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wants_newsletters', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wants_marketreport', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wants_dailyhitlist', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'reports', ['UserProfile'])

        # Adding model 'DealerMarketReport'
        db.create_table(u'reports_dealermarketreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dealer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Dealer'])),
            ('reportyearmonth', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.MarketReportYearMonth'])),
            ('marketreportshopimage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('marketreportdmmimage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('marketreportasiimage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('marketreportsocialimage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('marketreportutilityimage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('marketreportmiscimage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('marketreportmessage', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('marketreportnotes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('marketreportdescr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('marketreportinactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('marketreportdeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('marketreportcreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('marketreportupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['DealerMarketReport'])

        # Adding model 'DealerDailyHitList'
        db.create_table(u'reports_dealerdailyhitlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dealersite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.DealerSite'])),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('shopper_email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('shopper_phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('shopper_intensity', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('shopper_first_activity', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('shopper_last_lead_date', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('shopper_last_activity', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('shopper_last_site', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('shopper_preferred_vehicle', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('hitlistinactive', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('hitlistdeleted', self.gf('django.db.models.fields.CharField')(default='N', max_length=3, null=True)),
            ('hitlistcreatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('hitlistupdatedate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['DealerDailyHitList'])


    def backwards(self, orm):
        # Deleting model 'DataiumDMA'
        db.delete_table(u'reports_dataiumdma')

        # Deleting model 'DealerGroup'
        db.delete_table(u'reports_dealergroup')

        # Deleting model 'Dealer'
        db.delete_table(u'reports_dealer')

        # Deleting model 'DealerSite'
        db.delete_table(u'reports_dealersite')

        # Deleting model 'MarketReportYearMonth'
        db.delete_table(u'reports_marketreportyearmonth')

        # Deleting model 'UserProfile'
        db.delete_table(u'reports_userprofile')

        # Deleting model 'DealerMarketReport'
        db.delete_table(u'reports_dealermarketreport')

        # Deleting model 'DealerDailyHitList'
        db.delete_table(u'reports_dealerdailyhitlist')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'dataiumsiteid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dealercity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dealercreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dealerdeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'dealerdma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dealergroup': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Dealer Group'", 'null': 'True', 'to': u"orm['reports.DealerGroup']"}),
            'dealerinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dealerlat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'dealerlong': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'dealermainwebsite': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dealername': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dealerstate': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'dealerupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'dma': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'DMA'", 'null': 'True', 'to': u"orm['reports.DataiumDMA']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.dealerdailyhitlist': {
            'Meta': {'object_name': 'DealerDailyHitList'},
            'dealersite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.DealerSite']"}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hitlistcreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'hitlistdeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'hitlistinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True'}),
            'hitlistupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shopper_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shopper_first_activity': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'shopper_intensity': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'shopper_last_activity': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'shopper_last_lead_date': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'shopper_last_site': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shopper_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'shopper_preferred_vehicle': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'reports.dealergroup': {
            'Meta': {'object_name': 'DealerGroup'},
            'dataiumclientid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dealergroupcity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dealergroupcontactname': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'dealergroupcreatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dealergroupdeleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dealergroupinactive': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dealergroupname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dealergroupstate': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'dealergrouptype': ('django.db.models.fields.CharField', [], {'default': "'Auto Group'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'dealergroupupdatedate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
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
            'dataiumsitedescription': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
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
        },
        u'reports.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dealer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Dealer']", 'null': 'True', 'blank': 'True'}),
            'dealergroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.DealerGroup']", 'null': 'True', 'blank': 'True'}),
            'has_optedout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'wants_alerts': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wants_dailyhitlist': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wants_marketinfo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wants_marketreport': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wants_newsletters': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['reports']