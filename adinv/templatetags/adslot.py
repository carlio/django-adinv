from django import template
from django.template import Library, Node, TemplateSyntaxError
from adinv.models import AdSlot
from django.template.loader import render_to_string
import logging

register = Library()


class AdSlotNode(Node):
    def __init__(self, slot_name, *arguments, **kwargs):
        self.slot_name = slot_name
        self.arguments = arguments
        self.keyword_arguments = kwargs

    def _get_slot(self, context):
        try:
            slot_name = template.Variable(self.slot_name)
            slot_name = slot_name.resolve(context)
        except template.VariableDoesNotExist:
            raise ValueError
        
        try:
            return AdSlot.objects.get_for_name(slot_name=slot_name)
        except AdSlot.DoesNotExist:
            raise ValueError
        
    def render(self, context):
        slot = self._get_slot(context)
        if not slot.enabled:
            logging.debug('Ad slot %s is disabled' % slot)
            return ''
        
        advert = slot.get_advert(*self.arguments, **self.keyword_arguments)
        if advert is None:
            logging.debug('Could not get any adverts for %s' % slot)
            return ''
        
        local_ctx = {'slot': slot, 'advert': advert }
        return render_to_string('adinv/adslot.html', local_ctx, context)


@register.tag("adslot")
def adslot(parser, token):
    parts = token.split_contents()[1:]
    
    if len(parts) == 0:
        raise TemplateSyntaxError("'adslot' requires a slot name as the first argument")
    
    slot_name = parts[0]
    arguments = parts[1:]
    return AdSlotNode(slot_name, *arguments)


def adslot_string(slot_name, *args, **kwargs):
    """
    Utility method to render an adslot as a string, for use
    when templates and therefore template tags are not being used 
    """
    # need to wrap the slot name with quotes so that it is properly
    # resolved in the node
    return AdSlotNode("'%s'" % slot_name, *args, **kwargs).render({})