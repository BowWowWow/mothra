from django.contrib import admin

# Register your models here.

from .models import Dealer,DataiumDMA, DealerSite, MarketReportYearMonth,DealerMarketReport

class DataiumDMAAdmin(admin.ModelAdmin):
    list_display = ('dataiumdmaid','dmaname')

class DealerSiteAdmin(admin.ModelAdmin):
    list_display = ('dealer','dataiumsiteid','dataiumsitedescription')

class DealerAdmin(admin.ModelAdmin):
    list_display = ('dealername','dealercity','dealerstate','dealerinactive')

class MarketReportInline(admin.TabularInline):
    model=DealerMarketReport

class MarketReportYearMonthAdmin(admin.ModelAdmin):
    inlines = [
         MarketReportInline,
    ]


admin.site.register(Dealer,DealerAdmin)
admin.site.register(DataiumDMA,DataiumDMAAdmin)
admin.site.register(DealerSite,DealerSiteAdmin)
admin.site.register(MarketReportYearMonth,MarketReportYearMonthAdmin)
admin.site.register(DealerMarketReport)
