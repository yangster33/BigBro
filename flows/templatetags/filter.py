
from django import template

from costs.models import Costs

register = template.Library()


@register.filter(name='sum')
def sum(cost):

    return Costs.sum_cost(cost)

@register.filter(name='dot')
def dot(text):
    if len(text) > 11:
        return text[:12] + '...'
    else:
        return text
