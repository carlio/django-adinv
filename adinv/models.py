from django.db import models
from django.conf import settings


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
        
    

class AdSlot(models.Model):
    
    objects = AdSlotManager()
    
    slot_name = models.CharField(max_length=255, unique=True)
    dimensions = models.ForeignKey(SlotDimensions, null=True)
    enabled = models.BooleanField(default=False)
    
    ad_chooser = models.CharField(max_length=100)
    
    def get_possible_adverts(self):
        return Advert.objects.filter(enabled=True, dimensions=self.dimensions)
    
    def __unicode__(self):
        return self.slot_name
    
    
class Advert(models.Model):

    name = models.CharField(max_length=200)    
    dimensions = models.ForeignKey(SlotDimensions)
    code = models.TextField()
    enabled = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name


