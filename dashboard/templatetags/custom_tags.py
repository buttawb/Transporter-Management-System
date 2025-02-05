from django import template
# from dashboard.models import User_Image

# register = template.Library()


# @register.simple_tag
# def user_profile_image(user):
#     try:
#         user_image = User_Image.objects.get(user=user)
#         return user_image.img.url

#     except User_Image.DoesNotExist:
#         return '/static/images/user.png'
