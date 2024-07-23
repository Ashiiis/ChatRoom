# chat/middleware.py

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from .models import UserStatus

class UpdateLastActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            UserStatus.objects.update_or_create(user=request.user, defaults={'last_activity': timezone.now()})
        return None
