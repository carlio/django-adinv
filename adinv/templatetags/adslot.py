from django import template
from django.template import Library, Node, TemplateSyntaxError
from adinv.models import AdSlot

register = Library()


class AdSlotNode(Node):
    def __init__(self, slot_name, *arguments):
        self.slot_name = slot_name
        self.arguments = arguments

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
        return u'ADVERT! %s' % slot


@register.tag("adslot")
def adslot(parser, token):
    parts = token.split_contents()[1:]
    
    if len(parts) == 0:
        raise TemplateSyntaxError("'adslot' requires a slot name as the first argument")
    
    slot_name = parts[0]
    arguments = parts[1:]
    print type(slot_name), slot_name
    print type(parts[1]), parts[1]
    return AdSlotNode(slot_name, *arguments)
