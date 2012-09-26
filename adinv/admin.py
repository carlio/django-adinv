from django.contrib import admin
from adinv.models import AdSlot, SlotDimensions


class AdSlotAdmin(admin.ModelAdmin):
    list_filter = ('automatically_created',)
    list_display = ('slot_name', 'dimensions', 'enabled')

admin.site.register(AdSlot, AdSlotAdmin)

class SlotDimensionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlotDimensions, SlotDimensionsAdmin)