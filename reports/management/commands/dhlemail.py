from django.core.management.base import BaseCommand, CommandError

from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

from reports.models import Dealer,UserProfile,DealerSite,DealerDailyHitList, DealerGroup
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Sends Daily Hit List email to all subscribers'

    def add_arguments(self,parser):
        parser.add_argument('user_id',nargs='+',type=int)

    def handle(self, *args, **options):
        dhlrecipients = User.objects.filter(userprofile__wants_dailyhitlist=True)  
       

        for user in dhlrecipients:
            
            if user.userprofile.dealer:
                try:
                    dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N',username=user)
                    subject = "Dataium Daily Ups List"
                    dhldealer = dealeruser.userprofile.dealer
                    dhlsite = DealerSite.objects.filter(dealer = dhldealer)
                    dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5]
                    
                    # loginpurl = request.build_absolute_uri(reverse('django.contrib.auth.views.login'))
                    loginpurl = "https://calm-escarpment-8924.herokuapp.com/accounts/login/"                 

                    to = []
                    to = dealeruser.email.split(',')
                    from_email = 'no-reply@dataium.com'
                    ctx = {
                        'dealer':dhldealer,
                        'loginpurl':loginpurl,
                        'dhl':dhl,
                    }

                    message = get_template('client_dhlemail.html').render(Context(ctx))
                    msg = EmailMessage(subject,message,to=to,from_email=from_email)
                    msg.content_subtype = 'html'
                    msg.send()
                except:
                    print "dealer user is inactive or is not subscribed"
                
            if user.userprofile.dealergroup:
                try:
                    dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealergroup__dealergroupinactive='N',userprofile__dealergroup__dealergroupdeleted='N',username=user)

                    subject = "Dataium Daily Ups List"
                    dhldealergroup = dealeruser.userprofile.dealergroup
                    dhldealers = Dealer.objects.filter(dealergroup = dhldealergroup)
                    dhlsite = DealerSite.objects.filter(dealer = dhldealers)
                    dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5]      
                    # loginpurl = request.build_absolute_uri(reverse('django.contrib.auth.views.login'))
                    loginpurl = "https://calm-escarpment-8924.herokuapp.com/accounts/login/"
                    to = []
                    to = dealeruser.email.split(',')
                    from_email = 'no-reply@dataium.com'
                    ctx = {
                        'dealer':dhldealergroup,
                        'loginpurl':loginpurl,
                        'dhl':dhl,
                    }

                    message = get_template('client_dhlemail.html').render(Context(ctx))
                    msg = EmailMessage(subject,message,to=to,from_email=from_email)
                    msg.content_subtype = 'html'
                    msg.send()
                
                except:
                    print "group user is inactive or is not subscribed"




