from django.template import Library

register = Library()

def adslot():
    pass

register.inclusion_tag('adinv/inclusion/adslot.html')(adslot)
