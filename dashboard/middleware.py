from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that don't require authentication
        excluded_paths = [
            reverse('login'),
            # reverse('signup'),
        ]

        # If the user is not authenticated and the path is not excluded
        if not request.user.is_authenticated and request.path not in excluded_paths:
            return redirect('login')

        response = self.get_response(request)
        return response
