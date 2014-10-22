from django.conf.urls import patterns, include, url

from reports import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mothra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # note that to access urls here you'll need to preface with "reports/"
    url(r'^site/dhl/?$','reports.views.user_dhl',name='user_dhl'),
    url(r'^site/dhl/download/$','reports.views.dhl_file',name='dhl_file'),

    url(r'^forgot-password/$','forgot_password',name='forgot-password'),


)
