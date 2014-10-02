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

# jpb, 10/1/2014, added password reset imports
# from django.contrib.auth.views import password_reset, password_reset_confirm
# from django.contrib.auth.views import password_reset as django_password_reset
# from reports.forms import CustomPasswordResetForm


from django.contrib.auth.views import password_reset


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

# TO-DO, add authentication requirement

@login_required
def user_dhl(request):

    user_id = request.user.id

    try:
        dealeruser = User.objects.get(id=user_id,userprofile__wants_dailyhitlist=True,userprofile__dealer__dealerinactive='N',userprofile__dealer__dealerdeleted='N')
        dhldealer = dealeruser.userprofile.dealer        
        dhldealersite = DealerSite.objects.get(dealer = dhldealer)
        dhlleads = DealerDailyHitList.objects.filter(dealersite=dhldealersite)

    except ObjectDoesNotExist:
        print 'User id requested does not exist or is not subscribed to dhl'
        raise Http404

    return render_to_response('userdhl.html',locals(),context_instance=RequestContext(request))  




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
