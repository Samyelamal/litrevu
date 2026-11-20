from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from authentication.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'flux/',
        login_required(TemplateView.as_view(template_name='flux.html')),
        name='flux',
    ),
    path('signup/', signup_view, name='signup'),
]
