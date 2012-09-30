from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('adinv.views',
    url(r'^(?P<slot_id>\d+)/(?P<advert_id>\d+)$', 'advert_detail', name='advert_detail'),
    url(r'^(?P<impression_id>\d+)/click$', 'advert_click', name='advert_click'),
)