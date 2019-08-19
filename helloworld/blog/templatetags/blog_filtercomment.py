from django import template
# from django.db.models.query import QuerySet
from blog.models import Blog

register = template.Library()

# @register.filter
# def field_type(bound_field):
#     return bound_field.field.widget.__class__.__name__

@register.filter
def filtercomments(bound_field):
    if isinstance(bound_field, Blog):
        if bound_field.blog_comment.all()[0:1]:
            return True
        # return False
    return False
