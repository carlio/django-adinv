from django.db import models
from django.conf import settings


class SlotDimensionsManager(models.Manager):
    
    def get_default_dimensions(self):
        try:
            return self.get(name='default')
        except SlotDimensions.DoesNotExist:
            return self.create(name='default', width=0, height=0)
        

class SlotDimensions(models.Model):
    class Meta:
        verbose_name_plural = "Slot dimensions"
    
    objects = SlotDimensionsManager()
    
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
            return AdSlot.objects.create(slot_name=slot_name, 
                                         dimensions=SlotDimensions.objects.get_default_dimensions(),
                                         automatically_created=True)
        
    

class AdSlot(models.Model):
    
    objects = AdSlotManager()
    
    slot_name = models.CharField(max_length=255, unique=True)
    dimensions = models.ForeignKey(SlotDimensions)
    
    automatically_created = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.slot_name