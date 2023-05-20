from django import template
from index.models import MainHeader

register = template.Library()


@register.simple_tag()
def get_contact_data():
    return MainHeader.objects.get(pk=1)
