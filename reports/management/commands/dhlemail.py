from django.core.management.base import BaseCommand, CommandError

# from optparse import OptionParser

from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

from reports.models import Dealer,UserProfile,DealerSite,DealerDailyHitList, DealerGroup
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Send the daily hit list email."
    args = '<user_id user_id...> or <all>'
    # def add_arguments(self,parser):
    #     parser.add_argument('user_id',nargs='+',type=int)

    # option_list = BaseCommand.option_list + (make_option("-a","--all",dest="all",help="send to all users",default=False),)
    # option_list = option_list + (make_option("-i","--id",dest="id",help="send to specified user id"),)


    def handle(self, *args, **options):

        for user_id in args:
            if user_id == 'all':
                print 'Sending all users.'
                # find only users that are opting in
                dhlrecipients = User.objects.filter(userprofile__wants_dailyhitlist=True)
                # begin sending mails
                for user in dhlrecipients:

                    subject = "Dataium Daily Ups List"
                    loginpurl = "https://calm-escarpment-8924.herokuapp.com/accounts/login/"

                    # if the user belongs to a dealer then run this
                    if user.userprofile.dealer:
                        try:
                            dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N',username=user)
                            dhldealer = dealeruser.userprofile.dealer
                            dhlsite = DealerSite.objects.filter(dealer = dhldealer)
                            dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5]
	                    ctx = {
	                            'dealer':dhldealer,
	                            'loginpurl':loginpurl,
	                            'dhl':dhl,
	                        }


                        except:
                            print 'User is not subscribed, inactive, or dealer is inactive.'
                    # user belongs to a dealergroup, not a dealer
                    if user.userprofile.dealergroup:
                        try:
                            dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealergroup__dealergroupinactive='N',userprofile__dealergroup__dealergroupdeleted='N',username=user)
                            dhldealergroup = dealeruser.userprofile.dealergroup
                            dhldealers = Dealer.objects.filter(dealergroup = dhldealergroup)
                            dhlsite = DealerSite.objects.filter(dealer = dhldealers)
                            dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5]
	                    ctx = {
	                            'dealer':dhldealergroup,
	                            'loginpurl':loginpurl,
	                            'dhl':dhl,
	                        }

                        except:
                            print 'User is not subscribed, inactive, or dealer group is inactive.'
                    
                    # set up email - note there's a little difference to pass correct values for dealer vs. dealergroup

                    to = []
                    to = dealeruser.email.split(',')
                    from_email = 'no-reply@dataium.com'
                    
                    message = get_template('client_dhlemail.html').render(Context(ctx))
                    msg = EmailMessage(subject,message,to=to,from_email=from_email)
                    msg.content_subtype = 'html'
                    msg.send()
                    print 'Sent email to: ',to
  
            # all was not passed, so use specified ids
            else:
                print user_id
                dhlrecipients = User.objects.filter(userprofile__wants_dailyhitlist=True,id=user_id)
                print dhlrecipients
 
                for user in dhlrecipients:

                    subject = "Dataium Daily Ups List"
                    loginpurl = "https://calm-escarpment-8924.herokuapp.com/accounts/login/"

                    # if the user belongs to a dealer then run this
                    if user.userprofile.dealer:
                        try:
                            dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N',username=user)
                            dhldealer = dealeruser.userprofile.dealer
                            dhlsite = DealerSite.objects.filter(dealer = dhldealer)
                            dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5]
	                    ctx = {
	                            'dealer':dhldealer,
	                            'loginpurl':loginpurl,
	                            'dhl':dhl,
	                        }


                        except:
                            print 'User is not subscribed, inactive, or dealer is inactive.'
                    # user belongs to a dealergroup, not a dealer
                    if user.userprofile.dealergroup:
                        try:
                            dealeruser = User.objects.get(userprofile__wants_dailyhitlist=True,userprofile__dealergroup__dealergroupinactive='N',userprofile__dealergroup__dealergroupdeleted='N',username=user)
                            dhldealergroup = dealeruser.userprofile.dealergroup
                            dhldealers = Dealer.objects.filter(dealergroup = dhldealergroup)
                            dhlsite = DealerSite.objects.filter(dealer = dhldealers)
                            dhl = DealerDailyHitList.objects.filter(dealersite = dhlsite).order_by('-shopper_intensity')[:5]
	                    ctx = {
	                            'dealer':dhldealergroup,
	                            'loginpurl':loginpurl,
	                            'dhl':dhl,
	                        }

                        except:
                            print 'User is not subscribed, inactive, or dealer group is inactive.'
                    
                    # set up email - note there's a little difference to pass correct values for dealer vs. dealergroup

                    to = []
                    to = dealeruser.email.split(',')
                    from_email = 'no-reply@dataium.com'
                    
                    message = get_template('client_dhlemail.html').render(Context(ctx))
                    msg = EmailMessage(subject,message,to=to,from_email=from_email)
                    msg.content_subtype = 'html'
                    msg.send()
                    print 'Sent email to: ',to
 
   

