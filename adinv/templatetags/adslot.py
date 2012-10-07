from adinv.models import AdSlot
from django import template
from django.core.urlresolvers import reverse
from django.template import Library, Node, TemplateSyntaxError
from django.template.loader import render_to_string
from gubbins.utils import append_params
import logging

register = Library()


class AdSlotNode(Node):
    def __init__(self, slot_name, **kwargs):
        self.slot_name = slot_name
        self.keyword_arguments = kwargs

    def _resolve(self, name, context):
        try:
            return template.Variable(name).resolve(context)
        except template.VariableDoesNotExist:
            raise ValueError

    def _get_slot(self, context):
        slot_name = self._resolve(self.slot_name, context)

        try:
            return AdSlot.objects.get_for_name(slot_name=slot_name)
        except AdSlot.DoesNotExist:
            raise ValueError
        
    def render(self, context):
        slot = self._get_slot(context)
        if not slot.enabled:
            logging.debug('Ad slot %s is disabled' % slot)
            return ''
        
        # annoying method to append additional query parameters
        url = reverse('slot_detail', args=[slot.id])
        kwargs = {}
        for key, value in self.keyword_arguments.iteritems():
            kwargs[key] = self._resolve(value, context)
        url = append_params(url, kwargs)
        
        local_ctx = {'slot': slot, 'iframe_url': url }
        return render_to_string('adinv/adslot.html', local_ctx, context)


@register.tag("adslot")
def adslot(parser, token):
    parts = token.split_contents()[1:]
    
    if len(parts) == 0:
        raise TemplateSyntaxError("'adslot' requires a slot name as the first argument")
    
    slot_name = parts[0]
    arguments = parts[1:]
    kwargs = {}
    for argument in arguments:
        try:
            key, value = argument.split('=')
            kwargs[key] = value
        except ValueError:
            raise TemplateSyntaxError("'adslot' additional parameters must be of the form name=value")
        
    return AdSlotNode(slot_name, **kwargs)


def adslot_string(slot_name, *args, **kwargs):
    """
    Utility method to render an adslot as a string, for use
    when templates and therefore template tags are not being used 
    """
    # need to wrap the slot name with quotes so that it is properly
    # resolved in the node
    return AdSlotNode("'%s'" % slot_name, *args, **kwargs).render({})