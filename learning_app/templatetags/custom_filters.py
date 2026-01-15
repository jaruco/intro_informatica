from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Custom filter to get dictionary item in templates"""
    return dictionary.get(key)
