from django.contrib import admin
from adinv.models import AdSlot, SlotDimensions, Advert, Impression, Click



def enable(modeladmin, request, queryset):
    queryset.update(enabled=True)
enable.short_description = 'Enable selected'

def disable(modeladmin, request, queryset):
    queryset.update(enabled=False)
disable.short_description = 'Disable selected'



class AdSlotAdmin(admin.ModelAdmin):
    list_filter = ('dimensions', 'enabled',)
    list_display = ('slot_name', 'dimensions', 'ad_chooser', 'enabled')
    actions = (enable, disable)

admin.site.register(AdSlot, AdSlotAdmin)



class SlotDimensionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlotDimensions, SlotDimensionsAdmin)



class AdvertAdmin(admin.ModelAdmin):
    actions = (enable, disable)

admin.site.register(Advert, AdvertAdmin)


admin.site.register(Impression)
admin.site.register(Click)