from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import User
from django.contrib.auth.admin import UserAdmin

from .models import Dealer,DataiumDMA, DealerSite, MarketReportYearMonth,DealerMarketReport,UserProfile

class DataiumDMAAdmin(admin.ModelAdmin):
    list_display = ('dataiumdmaid','dmaname')

class DealerSiteAdmin(admin.ModelAdmin):
    list_display = ('dealer','dataiumsiteid','dataiumsitedescription')

class DealerAdmin(admin.ModelAdmin):
    list_display = ('dealername','dealercity','dealerstate','dealerinactive')

class MarketReportInline(admin.TabularInline):
    model=DealerMarketReport

def make_marketreport(modeladmin, request,queryset):
    # print object
    for object in queryset:
       ym = object
       d = Dealer.objects.filter(dealerinactive='N',dealerdeleted='N')
       for item in d:
           mkrpt = DealerMarketReport(dealer=item,reportyearmonth=ym)
           mkrpt.save()
    # self.message_user(request,"Market Reports Created")


make_marketreport.short_description = "Create Market Reports for Selected Year and Month"

class MarketReportYearMonthAdmin(admin.ModelAdmin):
    inlines = [
         MarketReportInline,
    ]
    actions = [make_marketreport]

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user profile'

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.register(Dealer,DealerAdmin)
admin.site.register(DataiumDMA,DataiumDMAAdmin)
admin.site.register(DealerSite,DealerSiteAdmin)
admin.site.register(MarketReportYearMonth,MarketReportYearMonthAdmin)
admin.site.register(DealerMarketReport)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
