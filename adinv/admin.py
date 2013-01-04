from django.contrib import admin
from adinv.models import AdSlot, SlotDimensions, Impression, Click,\
    JSAdvert, SimpleImageAdvert, AdvertConfigValue
from adinv.chooser.registry import registered_choosers




def enable(modeladmin, request, queryset):
    queryset.update(enabled=True)

def disable(modeladmin, request, queryset):
    queryset.update(enabled=False)

class AdSlotAdmin(admin.ModelAdmin):
    list_filter = ('dimensions', 'enabled',)
    list_display = ('slot_name', 'dimensions', 'ad_chooser', 'enabled')

    def get_actions(self, request):
        actions = super(AdSlotAdmin, self).get_actions(request)

        actions['enable'] = (enable, 'enable', 'Enable selected')
        actions['disable'] = (disable, 'disable', 'Disable selected')

        for dimension in SlotDimensions.objects.all():
            name = 'set_dimensions_to_%s' % dimension.name
            func = lambda modeladmin, request, queryset: queryset.update(dimensions=dimension)
            description = 'Set dimensions to %s' % dimension
            actions[name] = (func, name, description)

        for chooser in registered_choosers.keys():
            name = 'set_chooser_to_%s' % chooser
            func = lambda modeladmin, request, queryset: queryset.update(ad_chooser=chooser)
            description = 'Set chooser to %s' % chooser
            actions[name] = (func, name, description)

        return actions

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