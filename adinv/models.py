from adinv.chooser.registry import get_chooser, registered_choosers
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from gubbins.db.manager import InheritanceManager
import logging


class SlotDimensions(models.Model):
    class Meta:
        verbose_name_plural = "Slot dimensions"
    
    name = models.CharField(max_length=50)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()

    def __unicode__(self):
        return '%s (%sx%s)' % (self.name, self.width, self.height)


class AdSlotManager(models.Manager):
    
    def get_for_name(self, slot_name, create_override=None):
        if create_override is None:
            create = getattr(settings, 'ADINV_CREATE_MISSING_ADSLOTS', settings.DEBUG)
        else:
            create = create_override
            
        try:
            return self.get(slot_name=slot_name)
        except AdSlot.DoesNotExist:
            if not create:
                raise
            return AdSlot.objects.create(slot_name=slot_name, enabled=False)
        
    
    
_chooser_choices = [ (key, key) for key in registered_choosers.keys() ]

class AdSlot(models.Model):
    
    objects = AdSlotManager()
    
    slot_name = models.CharField(max_length=255, unique=True)
    dimensions = models.ForeignKey(SlotDimensions, null=True)
    enabled = models.BooleanField(default=False)
    
    ad_chooser = models.CharField(max_length=100, choices=_chooser_choices)
    
    def get_advert(self, *args, **kwargs):
        adverts = Advert.objects.filter(enabled=True, dimensions=self.dimensions)
        
        if adverts.count() == 0:
            logging.debug('No appropriate adverts available for %s' % self)
            return None
        
        logging.debug("Choosing from possible adverts: %s" % adverts)
        
        chooser = get_chooser(self.ad_chooser)
        if chooser is None:
            logging.debug('Could not find ad chooser %s' % self.ad_chooser)
            return None
        
        return chooser(self, adverts, *args, **kwargs)
    
    def __unicode__(self):
        return self.slot_name
    
    
class Advert(models.Model):

    objects = InheritanceManager()

    name = models.CharField(max_length=200)    
    dimensions = models.ForeignKey(SlotDimensions)
    enabled = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse('advert_detail', args=[self.id])
    
    def get_config(self):
        config = {}
        for cfg in self.advertconfigvalue_set.all():
            config[cfg.key] = cfg.value
        return config

    def __unicode__(self):
        return self.name
    


class SimpleImageAdvert(Advert):
    track_clicks = models.BooleanField(default=True)
    destination_url = models.CharField(max_length=500)
    image = models.ImageField(upload_to=getattr(settings, 'ADINV_IMAGE_MEDIA_PREFIX', 'inventory'))
    
    template_name = 'adinv/simple_image_advert_detail.html'
    
class JSAdvert(Advert):
    code = models.TextField()
    
    template_name = 'adinv/js_advert_detail.html'



class AdvertConfigValue(models.Model):
    advert = models.ForeignKey(Advert)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    
    def __unicode__(self):
        return '%s=%s' % (self.key, self.value)


class Impression(models.Model):
    advert = models.ForeignKey(Advert)
    adslot = models.ForeignKey(AdSlot)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s in %s at %s' % (self.advert, self.adslot, self.timestamp)
    
    
class Click(models.Model):
    impression = models.ForeignKey(Impression)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s in %s at %s' % (self.impression.advert, self.impression.adslot, self.timestamp)