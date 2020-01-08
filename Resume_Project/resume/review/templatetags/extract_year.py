from django import template

register = template.Library()

@register.filter(name='get_year')
def get_year(value):
    print('Get year is called')
    d = value.strftime("%m/%d/%Y")
    return d[-4:]