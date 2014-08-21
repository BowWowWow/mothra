from django.contrib import admin

# Register your models here.

from .models import Dealer,DataiumDMA

class DataiumDMAAdmin(admin.ModelAdmin):
    list_display = ('dataiumdmaid','dmaname')

admin.site.register(Dealer)
admin.site.register(DataiumDMA,DataiumDMAAdmin)
