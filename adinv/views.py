from django.shortcuts import get_object_or_404, render
from adinv.models import AdSlot


def slot_detail(request, slot_id):
    slot = get_object_or_404(AdSlot, pk=slot_id)
    advert = slot.get_advert(**request.GET)
    return render(request, advert.template_name, {'advert': advert})
