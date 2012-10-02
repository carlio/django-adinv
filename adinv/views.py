from django.shortcuts import get_object_or_404, render
from adinv.models import Advert


def advert_detail(request, advert_id):
    advert = get_object_or_404(Advert, pk=advert_id)
    return render(request, advert.template_name, {'advert': advert})
