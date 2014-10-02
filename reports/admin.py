from django.contrib import admin
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django import forms
from django.core.urlresolvers import reverse


# jpb, added for email actions to send bulk market report
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

# Register your models here.

from django.contrib.auth.admin import User
from django.contrib.auth.admin import UserAdmin

from .models import Dealer,DataiumDMA, DealerSite, MarketReportYearMonth,DealerMarketReport,UserProfile,DealerDailyHitList

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


class MarketReportYearMonthAdmin(admin.ModelAdmin):
    inlines = [
         MarketReportInline,
    ]
    
    class SendEmailForm(forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        category = forms.ModelChoiceField(MarketReportYearMonth.objects)


    def send_marketemail(self, request, queryset):
        print 'in send_marketemail'
        form = None

        if 'send' in request.POST:        
            form = self.SendEmailForm(request.POST)
            print 'in SEND'
 
                # send emails here
            if form.is_valid():
                print 'Sending EMAILS'
                # START OF SEND EMAILS
                tag = form.cleaned_data['category']
                count = 0
                for tag in queryset:
                     # client=Client.objects.get(id=client_id)
                     # hitlist = client.hitlist.all()
                     # search = client.search.all()
                     # newuseddata = client.newused.all()
                     subject = "Dataium Market Report for May 2014"
                     print tag
                     to = []
                     dealersend = Dealer.objects.filter(dealerinactive='N',dealerdeleted='N',userprofile__wants_marketreport=True)
                     print dealersend  
                     for item in dealersend:
                        # wow =  Dealer.objects.get(dealername = item.dealername)                 
                         userprof = UserProfile.objects.filter(dealer = item)
		         print userprof
                         user = User.objects.get(userprofile__in = userprof)
                         print user.email.split(',')
                         to = user.email.split(',')
                         
                     # bcc = ['support@dataium.com']
                         from_email = 'no-reply@dataium.com'
                         ctx = {
                         'client':item,
                         # 'hitlist':hitlist,
                         # 'search':search,
                         # 'newuseddata':newuseddata,
                         }
    
                         message = get_template('client_email.html').render(Context(ctx))
                     # msg = EmailMessage(subject,message,to=to,from_email=from_email,bcc=bcc)
                         msg = EmailMessage(subject,message,to=to,from_email=from_email)
                         msg.content_subtype = 'html'
                         msg.send()


                # END OF SEND EMAILS
                self.message_user(request,"Market Reports have been sent.")
                return HttpResponseRedirect(request.get_full_path())

        if not form:                            
            for object in queryset:
                ym = object
                d = Dealer.objects.filter(dealerinactive='N',dealerdeleted='N',userprofile__wants_marketreport=True)
        #  can I do "mkrpt = DealerMarketReport(d)?"
                mkrpt = DealerMarketReport.objects.filter(dealer__in = d)
                context = {'mkrpt':mkrpt,'mkrpt_form':ym,}
                print request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
                form = self.SendEmailForm(initial={'_selected_action':request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        return render_to_response('admin/send_marketreport.html', {'mkrpt':mkrpt,'mkrpt_form':form},context_instance=RequestContext(request))


    
    actions = ['make_marketreport','send_marketemail']
    send_marketemail.short_description = "Send Market Report"


# start of DHL sends
class DealerDailyHitListAdmin(admin.ModelAdmin):
    # inlines = [
    #      DealerDailyHitListInline,
    # ]
    
    
    def send_dhlemail(self, request, queryset):
        print 'in send_dhlemail'
        
        # get the list of daily hit list subscribers
        dealerusers = User.objects.filter(userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N')

        # for every user, build and send the email
        for user in dealerusers:
            subject = 'Dataium Daily Hit List' 
            dhldealer = user.userprofile.dealer
            loginpurl = request.build_absolute_uri(reverse('django.contrib.auth.views.login'))
            to = []
            to = user.email.split(',')
            from_email = 'no-reply@dataium.com'
            ctx = {
                'dealer':dhldealer,
                'loginpurl':loginpurl,
            }

            message = get_template('client_dhlemail.html').render(Context(ctx))
            msg = EmailMessage(subject,message,to=to,from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()


 

                # END OF SEND EMAILS
        self.message_user(request,"Market Reports have been sent.")
        return HttpResponseRedirect(request.get_full_path())

            
    actions = ['send_dhlemail']
    send_dhlemail.short_description = "Send Daily Hit List To All Users"


# end of DHL sends







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
admin.site.register(DealerDailyHitList,DealerDailyHitListAdmin)
