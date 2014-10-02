from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mothra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # jpb, added login/logout info
    # url(r'^accounts/login/$','django.contrib.auth.views.login',name='login'),
    # url(r'^accounts/logout/$','django.contrib.auth.views.logout',name='logout'),
    # url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),
    url('^accounts/', include('django.contrib.auth.urls')),
    url('',include('social.apps.django_app.urls',namespace='social')),

    # jpb, added reference to reports URLs
    url(r'^reports/',include('reports.urls',namespace='reports')),
    

)
