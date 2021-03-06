from django.contrib import admin
from adinv.models import AdSlot, SlotDimensions, Impression, Click,\
    JSAdvert, SimpleImageAdvert, AdvertConfigValue



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


class AdvertConfigInline(admin.TabularInline):
    model = AdvertConfigValue

class AdvertAdmin(admin.ModelAdmin):
    actions = (enable, disable)
    inlines = (AdvertConfigInline,)

admin.site.register(SimpleImageAdvert, AdvertAdmin)
admin.site.register(JSAdvert, AdvertAdmin)

class ImpressionAdmin(admin.ModelAdmin):
    fields = ( 'adslot', 'advert' )
    readonly_fields = ('timestamp', )
    list_filter = ( 'adslot', 'advert', 'timestamp')
    list_display = ( 'adslot', 'advert', 'timestamp')

admin.site.register(Impression, ImpressionAdmin)
admin.site.register(Click)