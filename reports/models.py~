from django.db import models

# Create your models here.



class DataiumDMA(models.Model):
     dataiumdmaid = models.IntegerField(default=0)
     dmaname = models.CharField(max_length=128)

     def __unicode__(self):
         return ''.join([str(self.dataiumdmaid),'-',self.dmaname,])



class Dealer(models.Model):
   dealername = models.CharField(max_length=128)
   dealercity = models.CharField(max_length=50)
   dealerstate = models.CharField(max_length=20)
   dealermainwebsite = models.CharField(max_length=50)
   dma = models.ForeignKey(DataiumDMA, related_name='dma')
   dealerdma = models.CharField(max_length=50)
   dealerlat = models.DecimalField(max_digits=10,decimal_places=6,null=True)
   dealerlong = models.DecimalField(max_digits=10,decimal_places=6,null=True)

   def __unicode__(self):
       return ''.join([self.dealername,' ',self.dealercity,', ',self.dealerstate,])
