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

from .models import Dealer,DataiumDMA, DealerSite, MarketReportYearMonth,DealerMarketReport,UserProfile,DealerDailyHitList,DealerGroup

class DataiumDMAAdmin(admin.ModelAdmin):
    list_display = ('dataiumdmaid','dmaname')
    search_fields = ['dmaname']

class DealerSiteAdmin(admin.ModelAdmin):
    list_display = ('dealer','dataiumsiteid','dataiumsitedescription')
    search_fields = ['dealer__dealername','dataiumsitedescription','dataiumsiteid']

class DealerAdmin(admin.ModelAdmin):
    list_display = ('dealername','dataiumsiteid','dealergroup','dealercity','dealerstate','dealerinactive')
    search_fields = ['dealername','dealergroup__dealergroupname','dealercity','dealerstate']

class DealerGroupAdmin(admin.ModelAdmin):
    list_display = ('dealergroupname','dataiumclientid','dealergroupcity','dealergroupstate','dealergroupinactive')
    search_fields = ['dealergroupname','dealergroupcity','dealergroupstate']


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







class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user profile'

class MyUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    actions = ['send_dhluseremail']

    # JPB, 2014-10-22, TO-DO:  Add logic for dealer group sends

    def send_dhluseremail(self,request,queryset):
        print 'in send_dhluseremail'
	users = queryset
        # get the list of daily hit list subscribers
        validusercount = 0
        invalidusercount = 0
        for user in queryset:

            if user.userprofile.dealer:
                print "user is dealer"
                try:
                    dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N',username=user)
                    subject = 'Dataium Daily Ups List' 
                    dhldealer = user.userprofile.dealer
            # get the list of dhl leads for presentation in the email
                    dhlsite = DealerSite.objects.filter(dealer = dhldealer)
                    dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5]
            # since we are going to the cloud, build the right link with host
                    loginpurl = request.build_absolute_uri(reverse('django.contrib.auth.views.login'))
                    to = []
                    to = user.email.split(',')
                    from_email = 'no-reply@dataium.com'
                    ctx = {
                        'dealer':dhldealer,
                        'loginpurl':loginpurl,
                        'dhl':dhl,
                    }

                    message = get_template('client_dhlemail.html').render(Context(ctx))
                    msg = EmailMessage(subject,message,to=to,from_email=from_email)
                    msg.content_subtype = 'html'
                    print "right before msg.send"
                    msg.send()
                    validusercount = validusercount +1

                # END OF SEND EMAILS

                except:
                    print "user is inactive or is not subscribed"
                    invalidusercount = invalidusercount + 1


            
            if user.userprofile.dealergroup:
                print "user is group"
                try:
                    dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealergroup__dealergroupinactive='N',userprofile__dealergroup__dealergroupdeleted='N',username=user)
                    
                    subject = 'Dataium Daily Hit List' 
                    dhldealergroup = user.userprofile.dealergroup
                    
            # get the list of dhl leads for presentation in the email
                    dhldealers = Dealer.objects.filter(dealergroup = dhldealergroup)
                    dhlsite = DealerSite.objects.filter(dealer = dhldealers)
                   
                    dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5] 
                                  
            # since we are going to the cloud, build the right link with host
                    loginpurl = request.build_absolute_uri(reverse('django.contrib.auth.views.login'))
                    print loginpurl
		    to = []
                    to = user.email.split(',')
                    from_email = 'no-reply@dataium.com'
                    ctx = {
                        'dealer':dhldealergroup,
                        'loginpurl':loginpurl,
                        'dhl':dhl,
                    }

                    message = get_template('client_dhlemail.html').render(Context(ctx))
                    msg = EmailMessage(subject,message,to=to,from_email=from_email)
                    msg.content_subtype = 'html'
                    print "right before msg.send"
                    msg.send()
                    validusercount = validusercount +1
                
                except:
                    print "user is inactive or is not subscribed"
                    invalidusercount = invalidusercount + 1

        self.message_user(request,"%s Daily Hit Lists have been sent." % validusercount)

    send_dhluseremail.short_description = "Send Daily Hit List To Selected Users"

# end of UserAdmin

admin.site.register(Dealer,DealerAdmin)
admin.site.register(DataiumDMA,DataiumDMAAdmin)
admin.site.register(DealerSite,DealerSiteAdmin)
admin.site.register(MarketReportYearMonth,MarketReportYearMonthAdmin)
admin.site.register(DealerMarketReport)
admin.site.register(DealerGroup,DealerGroupAdmin)
admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)

