from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from django.http import HttpResponse

# jpb, 10/1/2014, was getting reverse error for password reset.  added for this.
from django.core.urlresolvers import reverse

# jpb, 9/30/2014 added reports models
from reports.models import Dealer,UserProfile,DealerSite,DealerDailyHitList
from django.contrib.auth.models import User

# jpb, 9/30/2014 added for exception check if client id not found
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# jpb, 9/30/2014, added for login requirement
from django.contrib.auth.decorators import login_required

# jpb, 12/2/2014, added to format date in download files
from datetime import datetime
from django.utils import formats

# jpb, 10/1/2014, added password reset imports
# from django.contrib.auth.views import password_reset, password_reset_confirm
# from django.contrib.auth.views import password_reset as django_password_reset
# from reports.forms import CustomPasswordResetForm


from django.contrib.auth.views import password_reset

# jpb, 10/22/2014, added CSV library for lead downloads
import csv


# Create your views here.


# jpb, 10/1/2014, add password reset views

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('reports:login'))


# reuse Django view, but change form
def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request,from_email=request.POST.get('email'))
    else:
        return render(request,'forgot_password.html')



# jpb, 2014-09-30, added dhl view

# jpb, 2014-10-21, TO-DO:  Add logic to determine if user is a group user or dealer user.
@login_required
def user_dhl(request):

    user_id = request.user.id
    print user_id
    
    # JPB, NEED TO CHECK THE dealeruser object here....not in the exception loop
    try:
        dealeruser = User.objects.get(id=user_id,userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N')
        print 'executing standalone dealer'

        dhldealer = dealeruser.userprofile.dealer        
        dhldealersite = DealerSite.objects.get(dealer = dhldealer)
        dhlleads = DealerDailyHitList.objects.filter(dealersite=dhldealersite).order_by('dealersite','-shopper_intensity','-shopper_last_activity')
    except:
        
        try: 
            dealeruser = User.objects.get(id=user_id,userprofile__wants_dailyhitlist=True,userprofile__dealergroup__dealergroupinactive='N',userprofile__dealergroup__dealergroupdeleted='N')
            print 'this user is a member of a group!'
            dealergroup = dealeruser.userprofile.dealergroup
            print dealergroup
            dhldealer = Dealer.objects.filter(dealergroup=dealeruser.userprofile.dealergroup)
            print dhldealer
            dhldealersite = DealerSite.objects.filter(dealer=dhldealer)
            print dhldealersite 
            dhlleads = DealerDailyHitList.objects.filter(dealersite=dhldealersite).order_by('dealersite','-shopper_intensity','-shopper_last_activity')
        # print locals()
        except:
            print 'No query'
            dealeruser = None 

    return render_to_response('userdhl.html',locals(),context_instance=RequestContext(request))  



# jpb, 2014-10-22, added view to download file

@login_required
def dhl_file(request):

    user_id = request.user.id
    print user_id
    
    # JPB, NEED TO CHECK THE dealeruser object here....not in the exception loop
    try:
        dealeruser = User.objects.get(id=user_id,userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N')
        print 'executing standalone dealer'

        dhldealer = dealeruser.userprofile.dealer        
        dhldealersite = DealerSite.objects.get(dealer = dhldealer)
        dhlleads = DealerDailyHitList.objects.filter(dealersite=dhldealersite).order_by('dealersite','-shopper_intensity','-shopper_last_activity')
    except:
        dealeruser = User.objects.get(id=user_id,userprofile__wants_dailyhitlist=True,userprofile__dealergroup__dealergroupinactive='N',userprofile__dealergroup__dealergroupdeleted='N')
        print 'this user is a member of a group!'
        # dealergroup = dealeruser.userprofile.dealergroup
        dhldealers = Dealer.objects.filter(dealergroup=dealeruser.userprofile.dealergroup)
        dhldealersite = DealerSite.objects.filter(dealer=dhldealers)
        dhlleads = DealerDailyHitList.objects.filter(dealersite=dhldealersite).order_by('dealersite','-shopper_intensity','-shopper_last_activity')
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dhldownload.csv"'
    writer = csv.writer(response,quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['Shopper Name','Shopper EMail','Shopper Phone','Shopper Intensity','Shopper First Activity','Shopper Last Lead Date','Shopper Last Activity','Shopper Last Site','Shopper Preferred Vehicle','Dealer'])
    for row in dhlleads:

        if row.shopper_first_activity_date == None:
            shop_first_activity = ""
        else:
            shop_first_activity = row.shopper_first_activity_date.strftime("%m/%d/%Y")

        if row.shopper_last_lead_submitted_date == None:
            shop_last_lead_submitted_date = ""
        else:
            shop_last_lead_submitted_date = row.shopper_last_lead_submitted_date.strftime("%m/%d/%Y")

        if row.shopper_last_activity_date == None:
            shop_last_activity_date = ""
        else:
            shop_last_activity_date = row.shopper_last_activity_date.strftime("%m/%d/%Y")


        writer.writerow([row.full_name,row.shopper_email,row.shopper_phone,row.shopper_intensity,shop_first_activity,shop_last_lead_submitted_date, shop_last_activity_date,row.shopper_last_site,row.shopper_preferred_vehicle,row.dealersite])

    return response 



# jpb, changed to add exception check if client not found
#    try:
#    	client = Client.objects.get(id=client_id)
       
#   jpb, this worked
#        bogus_shops = client.shops.all()
 #       shops = serializers.serialize('json',bogus_shops)
  #      bogus_dmm = client.dmm.all()
   #     dmm = serializers.serialize('json',bogus_dmm)
    #    bogus_search = client.search.all()
#        search = serializers.serialize('json',bogus_search)
#        hitlist = client.hitlist.all()
#        newuseddata = client.newused.all()

#        return render_to_response('client.html',locals(),context_instance=RequestContext(request))
 #   except ObjectDoesNotExist:
#	print "Client id requested does not exist"
#        raise Http404
#    return HttpResponse("In site_dhl")
