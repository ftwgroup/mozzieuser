from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from contacts.resources import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mozzieserver.views.home', name='home'),
    # url(r'^mozzieserver/', include('mozzieserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('djangorestframework.urls', namespace='djangorestframework')),
    url(r'^people/$', ListOrCreateModelView.as_view(resource=ContactsResource)),
    url(r'^(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=ContactsResource), name='person'),
    url(r'^phone-numbers/$', ListOrCreateModelView.as_view(resource=PhoneNumberResource), name='phone_numbers'),
    url(r'^groups/$', ListOrCreateModelView.as_view(resource=GroupResource), name='groups'),
)
