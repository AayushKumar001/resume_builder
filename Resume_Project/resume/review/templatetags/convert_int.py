from django import template

register = template.Library()

@register.filter(name='times')
def cut_value(value):
    print('Value is:'+str(value))
    integer_value = int(value)
    return range(integer_value)