from django.contrib import admin
from django.shortcuts import render_to_response

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
    for object in queryset:
       ym = object
       # print ym
       d = Dealer.objects.filter(dealerinactive='N',dealerdeleted='N')
       for item in d:
           mkrpt = DealerMarketReport(dealer=item,reportyearmonth=ym)
           mkrpt.save()
    # self.message_user(request,"Market Reports Created")


make_marketreport.short_description = "Create Market Reports for Selected Year and Month"

def send_marketreport(modeladmin,request,queryset):
    form = None

    if 'send' in request.POST:
    
        if form.is_valid():
            for item in mkrpt:
                # do email stuff here
            
            self.message_user(request, "Successfully sent market reports.")
            return HttpResponseRedirect(request.get_full_path())


    if not form:
        
    for object in queryset:
        ym = object
        print ym
        d = Dealer.objects.filter(dealerinactive='N',dealerdeleted='N',userprofile__wants_marketreport=True)
        print d
        #  can I do "mkrpt = DealerMarketReport(d)?"
    mkrpt = DealerMarketReport.objects.filter(dealer__in = d)

    return render_to_response('admin/send_marketreport.html',{'mkrpt':mkrpt,'mkrpt_form':form,})

 
send_marketreport.short_description = "Send Market Reports for Selected Year and Month"

class MarketReportYearMonthAdmin(admin.ModelAdmin):
    inlines = [
         MarketReportInline,
    ]
    actions = [make_marketreport,send_marketreport]

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
