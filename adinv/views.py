from django.shortcuts import render, get_object_or_404
from adinv.models import Advert, AdSlot, Impression


def advert_detail(request, slot_id, advert_id):
    slot = get_object_or_404(AdSlot, pk=slot_id)
    advert = get_object_or_404(Advert, pk=advert_id)
    
    impression = Impression.objects.create(slot=slot, advert=advert)
    
    return render(request, 'adinv/advert_detail.html', {'advert': advert, 'slot': slot,
                                                        'impression': impression})

def advert_click(request, impression_id):
    pass