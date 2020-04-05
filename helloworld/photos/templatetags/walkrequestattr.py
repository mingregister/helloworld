from django import template

register = template.Library()

# @register.filter
# def field_type(bound_field):
#     return bound_field.field.widget.__class__.__name__

@register.filter(name='printtype')
def print_type(obj):
    return type(obj)

@register.filter
def walkattrs(request_attr):
    # print(type(request_attr))
    request_list = dir(request_attr)
    return request_list
