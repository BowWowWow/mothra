from django.db import models

# Create your models here.



class DataiumDMA(models.Model):
     dataiumdmaid = models.IntegerField(verbose_name='DMA ID',default=0)
     dmaname = models.CharField(verbose_name='DMA Name',max_length=128)
     dmainactive = models.CharField(verbose_name='DMA Inactive',max_length=3,null=True,default='N')
     dmadeleted = models.CharField(verbose_name='DMA Deleted',max_length=3,null=True,default='N')
     dmacreatedate = models.DateTimeField(verbose_name='DMA Created On',auto_now_add=True,null=True)
     dmaupdatedate = models.DateTimeField(verbose_name='DMA Updated On',auto_now=True,null=True)

     class Meta:
          verbose_name = "DMA"
     
     def __unicode__(self):
         return ''.join([str(self.dataiumdmaid),'-',self.dmaname,])



class Dealer(models.Model):
   dealername = models.CharField(verbose_name='Dealer Name',max_length=128)
   dealercity = models.CharField(verbose_name='Dealer City',max_length=50)
   dealerstate = models.CharField(verbose_name='Dealer State',max_length=20)
   dealermainwebsite = models.CharField(verbose_name='Dealer Main Site',max_length=50)
   dma = models.ForeignKey(DataiumDMA, related_name='DMA')
   dealerdma = models.CharField(verbose_name='DMA Description',max_length=50)
   dealerlat = models.DecimalField(verbose_name = 'Dealer Latitude',max_digits=10,decimal_places=6,null=True)
   dealerlong = models.DecimalField(verbose_name='Dealer Longitude',max_digits=10,decimal_places=6,null=True)
   dealerinactive = models.CharField(verbose_name='Dealer Inactive',max_length=3,null=True,default='N')
   dealerdeleted = models.CharField(verbose_name='Dealer Deleted',max_length=3,null=True,default='N')
   dealercreatedate = models.DateTimeField(verbose_name='Dealer Created On',auto_now_add=True,null=True)
   dealerupdatedate = models.DateTimeField(verbose_name='Dealer Updated On',auto_now=True,null=True)

   class Meta:
        verbose_name = "Dealer"

   def __unicode__(self):
       return ''.join([self.dealername,' ',self.dealercity,', ',self.dealerstate,])



class DealerSite(models.Model):
   dealer = models.ForeignKey(Dealer)
   dataiumsiteid = models.IntegerField(verbose_name='Dataium Site ID',default=0,null=True)
   dataiumsitedescription = models.CharField(verbose_name='Site Description (URL)',max_length=128,null=True)
   dealersiteinactive = models.CharField(verbose_name='Dealer Site Inactive',max_length=3,null=True,default='N')
   dealersitedeleted = models.CharField(verbose_name='Dealer Site Deleted',max_length=3,null=True,default='N')
   dealersitecreatedate = models.DateTimeField(verbose_name='Dealer Site Created On',auto_now_add=True,null=True)
   dealersiteupdatedate = models.DateTimeField(verbose_name='Dealer Site Updated On',auto_now=True,null=True)

   class Meta:
        verbose_name="Site"
   
   def __unicode__(self):
       return self.dataiumsitedescription


class MarketReportYearMonth(models.Model):
   MARKET_REPORT_YEAR_MONTH_CHOICES = (
       ('201405','May 2014'),
       ('201406','June 2014'),
       ('201407','July 2014'),
       ('201408','August 2014'),
       ('201409','September 2014'),
       ('201410','October 2014'),
       ('201411','November 2014'),
       ('201412','December 2014'),
       ('201501','January 2015'),
       ('201502','February 2015'),
       ('201503','March 2015'),
       ('201504','April 2015'),
       ('201505','May 2015'),
       ('201506','June 2015'),
       ('201507','July 2015'),
       ('201508','August 2015'),
       ('201509','September 2015'),
       ('201510','October 2015'),
       ('201511','November 2015'),
       ('201512','December 2015'),
       ('201601','January 2016'),
       ('201602','February 2016'),
       ('201603','March 2016'),
       ('201604','April 2016'),
       ('201605','May 2016'),
       ('201606','June 2016'),
       ('201607','July 2016'),
       ('201608','August 2016'),
       ('201609','September 2016'),
       ('201610','October 2016'),
       ('201611','November 2016'),
       ('201612','December 2016'),
   )

   marketreportyearmonthchar = models.CharField(max_length=6,choices=MARKET_REPORT_YEAR_MONTH_CHOICES,null=True,verbose_name='Market Report Year Month',unique=True)
   marketreportyearmonthinactive = models.CharField(verbose_name='Market Report Year Month Inactive',default='N',null=True,max_length=3)
   marketreportyearmonthdeleted = models.CharField(verbose_name='Market Report Year Month Deleted',max_length=3,null=True,default='N')
   marketreportyearmonthcreatedate = models.DateTimeField(verbose_name='Market Report Year Month Created On',auto_now_add=True,null=True)
   marketreportyearmonthupdatedate = models.DateTimeField(verbose_name='Market Report Year Month Updated On',auto_now=True,null=True)

   @property
   def marketreportyearmonthdesc(self):
       if self.marketreportyearmonthchar == '201405':
           yymm = 'May 2014'
       elif self.marketreportyearmonthchar == '201406':
           yymm = 'June 2014'
       elif self.marketreportyearmonthchar == '201407':
           yymm = 'July 2014'
       elif self.marketreportyearmonthchar == '201408':
           yymm = 'August 2014'
       elif self.marketreportyearmonthchar == '201409':
           yymm = 'September 2014'
       elif self.marketreportyearmonthchar == '201410':
           yymm = 'October 2014'
       elif self.marketreportyearmonthchar == '201411':
           yymm = 'November 2014'
       elif self.marketreportyearmonthchar == '201412':
           yymm = 'December 2014'
       elif self.marketreportyearmonthchar == '201501':
           yymm = 'January 2015'
       elif self.marketreportyearmonthchar == '201502':
           yymm = 'February 2015'
       elif self.marketreportyearmonthchar == '201503':
           yymm = 'March 2015'
       elif self.marketreportyearmonthchar == '201504':
           yymm = 'April 2015'
       elif self.marketreportyearmonthchar == '201505':
           yymm = 'May 2015'
       elif self.marketreportyearmonthchar == '201506':
           yymm = 'June 2015'
       elif self.marketreportyearmonthchar == '201507':
           yymm = 'July 2015'
       elif self.marketreportyearmonthchar == '201508':
           yymm = 'August 2015'
       elif self.marketreportyearmonthchar == '201509':
           yymm = 'September 2015'
       elif self.marketreportyearmonthchar == '201510':
           yymm = 'October 2015'
       elif self.marketreportyearmonthchar == '201511':
           yymm = 'November 2015'
       elif self.marketreportyearmonthchar == '201512':
           yymm = 'December 2015'
       elif self.marketreportyearmonthchar == '201601':
           yymm = 'January 2016'
       elif self.marketreportyearmonthchar == '201602':
           yymm = 'February 2016'
       elif self.marketreportyearmonthchar == '201603':
           yymm = 'March 2016'
       elif self.marketreportyearmonthchar == '201604':
           yymm = 'April 2016'
       elif self.marketreportyearmonthchar == '201605':
           yymm = 'May 2016'
       elif self.marketreportyearmonthchar == '201606':
           yymm = 'June 2016'
       elif self.marketreportyearmonthchar == '201607':
           yymm = 'July 2016'
       elif self.marketreportyearmonthchar == '201608':
           yymm = 'August 2016'
       elif self.marketreportyearmonthchar == '201609':
           yymm = 'September 2016'
       elif self.marketreportyearmonthchar == '201610':
           yymm = 'October 2016'
       elif self.marketreportyearmonthchar == '201611':
           yymm = 'November 2016'
       elif self.marketreportyearmonthchar == '201612':
           yymm = 'December 2016'
       return yymm

   class Meta:
        verbose_name="Market Report Timeframe"

   def __unicode__(self):
        return self.marketreportyearmonthdesc


# jpb, 6/14/2014 added class for market report
class DealerMarketReport(models.Model):
   dealer = models.ForeignKey(Dealer)
   # userprofile = models.ForeignKey(UserProfile)
   reportyearmonth = models.ForeignKey(MarketReportYearMonth)
   marketreportshopimage = models.CharField(max_length=100,editable=False)
   marketreportdmmimage = models.CharField(max_length=100,editable=False)
   marketreportasiimage = models.CharField(max_length=100,editable=False)
   marketreportsocialimage = models.CharField(max_length=100,editable=False)
   marketreportutilityimage = models.CharField(max_length=100,editable=False)
   marketreportmiscimage = models.CharField(max_length=100,editable=False)
   marketreportmessage = models.CharField(verbose_name='Message',max_length=200, null=True,blank=True)
   marketreportnotes = models.CharField(verbose_name='Notes',max_length=200, null=True,blank=True)
   marketreportdescr = models.CharField(verbose_name = 'Description',max_length=200, null=True,blank=True)
   marketreportinactive = models.CharField(verbose_name='Market Report Inactive',default='N',null=True,max_length=3)
   marketreportdeleted = models.CharField(verbose_name='Market Report Deleted',max_length=3,null=True,default='N')
   marketreportcreatedate = models.DateTimeField(verbose_name='Market Report Created On',auto_now_add=True,null=True)
   marketreportupdatedate = models.DateTimeField(verbose_name='Market Report Updated On',auto_now=True,null=True)



   class Meta:
       verbose_name="Market Report"

   def __unicode__(self):
       return ''.join([self.dealer.dealername,' ',self.reportyearmonth.marketreportyearmonthdesc])

   def save(self):
       super(DealerMarketReport,self).save
       self.marketreportdmmimage = ''.join(['dealer_dmm_',str(self.dealer.id),'_',self.reportyearmonth.marketreportyearmonthchar])
       self.marketreportshopimage = ''.join(['dealer_shops_',str(self.dealer.id),'_',self.reportyearmonth.marketreportyearmonthchar])
       self.marketreportasiimage = ''.join(['dealer_asi_',str(self.dealer.id),'_',self.reportyearmonth.marketreportyearmonthchar])
       self.marketreportsocialimage = ''.join(['dealer_search_',str(self.dealer.id),'_',self.reportyearmonth.marketreportyearmonthchar])
       self.marketreportutilityimage = ''.join(['dealer_util_',str(self.dealer.id),'_',self.reportyearmonth.marketreportyearmonthchar])
       self.marketreportmiscimage = ''.join(['dealer_misc_',str(self.dealer.id),'_',self.reportyearmonth.marketreportyearmonthchar])
       super(DealerMarketReport,self).save()


