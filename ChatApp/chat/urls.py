from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("chat/", chat_views.chatPage, name="chat-page"),

    # login-section
    path("", chat_views.defaultpage, name="landing_page"),
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(template_name="chat/"), name="logout-user"),
    path('online-users/', chat_views.online_users, name='online_users'),

]
# all the paths to the templates and view functions are compiled here with clear name