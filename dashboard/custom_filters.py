from django import template

register = template.Library()


@register.filter
def get_item_for_i(queryset, index):
    try:
        return queryset[index]['train']['i_completed_date']
    except (KeyError, IndexError):
        return None
