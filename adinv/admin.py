from django.contrib import admin
from adinv.models import AdSlot, SlotDimensions, Advert


class AdSlotAdmin(admin.ModelAdmin):
    list_filter = ('enabled',)
    list_display = ('slot_name', 'dimensions', 'enabled')

admin.site.register(AdSlot, AdSlotAdmin)

class SlotDimensionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlotDimensions, SlotDimensionsAdmin)

class AdvertAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advert, AdvertAdmin)