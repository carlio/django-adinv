from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('adinv.views',
    url(r'^(?P<advert_id>\d+)$', 'advert_detail', name='advert_detail'),
)
