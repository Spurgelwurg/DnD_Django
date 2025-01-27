from django import template
"""
Custom template tags for the DnD_Django game application.
This module contains a custom filter for debugging purposes.
Filters:
    debug_print: Returns the list of attributes and methods of the given value.
Usage:
    <pre>
        {{ form|debug_print }}
    </pre>
"""

register = template.Library()

@register.filter
def debug_print(value):
    return dir(value)