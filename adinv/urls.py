from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('adinv.views',
    url(r'^(?P<slot_id>\d+)$', 'slot_detail', name='slot_detail'),
)
