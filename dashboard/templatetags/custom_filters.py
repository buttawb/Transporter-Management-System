from django import template
from datetime import datetime, timedelta

register = template.Library()


# Filter to check if the date is expired
@register.filter(name='is_expired')
def is_expired(value):
    if value:
        return value < datetime.now().date()
    return False


# Filter to check if the date is close to expiring (e.g., within 30 days)
@register.filter(name='is_soon_expiring')
def is_soon_expiring(value):
    if value:
        return value < datetime.now().date() + timedelta(days=30) and value >= datetime.now().date()
    return False


# Filter to check if the date is valid (i.e., not expired or close to expiring)
@register.filter(name='is_valid')
def is_valid(value):
    if value:
        return value >= datetime.now().date() + timedelta(days=30)
    return False
