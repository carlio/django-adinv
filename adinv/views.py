from django.shortcuts import get_object_or_404, redirect, render
from adinv.models import Advert, AdSlot, Impression, Click


def advert_detail(request, slot_id, advert_id):
    slot = get_object_or_404(AdSlot, pk=slot_id)
    advert = get_object_or_404(Advert, pk=advert_id)
    
    impression = Impression.objects.create(adslot=slot, advert=advert)
    
    return render(request, advert.template_name, {'advert': advert, 'slot': slot,
                                                        'impression': impression})

def advert_click(request, impression_id):
    impression = get_object_or_404(Impression, pk=impression_id)
    Click.objects.create(impression=impression)
    advert = Advert.objects.get(pk=impression.advert.id)
    
    return redirect(advert.destination_url)