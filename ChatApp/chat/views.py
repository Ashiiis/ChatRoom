from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserStatus

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)
def online_users(request):
    online_users = [status.user for status in UserStatus.objects.all() if status.is_online()]
    return render(request, 'chat/online_users.html', {'online_users': online_users})
def defaultpage(request):
    return render(request, 'chat/LandingPage.html')