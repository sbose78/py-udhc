from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^new_health_report.udhc', 'openshift.views.new_health_report', name='new_health_report'),
    url(r'^new_narrative.udhc', 'openshift.views.new_narrative', name='new_narrative'),
    url(r'^health_case.udhc', 'openshift.views.health_case', name='health_case'),
    url(r'^submit_health_case.udhc', 'openshift.views.process_health_case', name='process_health_case'),
    url(r'^health_record.udhc', 'openshift.views.health_record', name='health_record'),
    url(r'^add_more_reports.udhc', 'openshift.views.add_more_reports', name='add_more_reports'),
    url(r'^my_image/(?P<image_id>.*)$', 'openshift.views.my_image', name='my_image'),
    url(r'^(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT }),
    # url(r'^openshift/', include('openshift.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)