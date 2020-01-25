
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

@register.filter(name='split')
def split(flows,index):
    try:
        return flows.split('-')[index+1]
    except IndexError:
        return '最终流程'

@register.filter(name='per')
def per(flows,index):
    length = len(flows.split('-'))
    return int(round(100*index/length, 0))

@register.filter(name='per2')
def per2(flows,index):
    '''0/5---(0%)'''
    length = len(flows.split('-'))
    return str(index)+'/'+str(length)+'---('+str(int(round(100*index/length, 0)))+'%)'


