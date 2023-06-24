from django import template

register = template.Library()

@register.filter(name='get_range')
def get_range(number):
    return range(number)

@register.filter(name='get_from_dict')
def get_from_dict(my_dict, i):
    return my_dict[i]

@register.filter(name='first_char')
def first_char(s):
    return str(s)[0]