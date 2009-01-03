from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^post/$', 'recaptcha_comments.views.validate_and_submit'),
    (r'^', include('django.contrib.comments.urls')),
)
