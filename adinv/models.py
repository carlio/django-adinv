from django.db import models

class AdDimensions(models.Model):
    name = models.CharField(max_length=50)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()

    def __unicode__(self):
        return '%s (%sx%s)' % (self.name, self.width, self.height)
    

class AdSlot(models.Model):
    slot_name = models.CharField(max_length=255, unique=True)
    dimensions = models.ForeignKey(AdDimensions)
    
    def __unicode__(self):
        return self.slot_name