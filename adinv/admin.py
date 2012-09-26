from django.contrib import admin
from adinv.models import AdSlot, SlotDimensions


class AdSlotAdmin(admin.ModelAdmin):
    filter_fields = ('automatically_created',)

admin.site.register(AdSlot, AdSlotAdmin)

class SlotDimensionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlotDimensions, SlotDimensionsAdmin)