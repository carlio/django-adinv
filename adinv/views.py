from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from adinv.models import AdSlot, Impression, Advert


def slot_detail(request, slot_id):
    slot = get_object_or_404(AdSlot, pk=slot_id)
    advert = slot.get_advert(**request.GET)

    if advert.track_clicks:
        impression = advert.add_impression(slot)
        dest_url = reverse('advert_track_click', args=[impression.id])
    else:
        dest_url = advert.destination_url

    return render(request, advert.template_name, {'advert': advert, 'dest_url': dest_url})

def advert_track_click(request, impression_id):
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.add_click()
    advert = Advert.objects.get(id=impression.advert.id) # needed to downcast correctly
    return redirect(advert.destination_url)