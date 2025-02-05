from django import template
from dashboard.models import UserImage

register = template.Library()


@register.simple_tag
def user_profile_image(user):
    try:
        user_image = UserImage.objects.get(user=user)
        return user_image.img.url

    except UserImage.DoesNotExist:
        return '/static/images/user.png'
