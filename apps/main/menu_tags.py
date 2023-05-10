from django import template
from .models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html')
def menu_items():
    menu_items = MenuItem.objects.all()
    return { 'menu_items': menu_items }

@register.inclusion_tag('menu_item.html')
def menu_item(item, selected_item=None):
    return { 'item': item, 'selected_item': selected_item }

@register.simple_tag(takes_context=True)
def is_selected(context, item):
    request = context['request']
    return 'active' if request.path == item.url else ''