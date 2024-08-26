"""websock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from chat import views as chat_views

class LogoutView(auth_views.LogoutView):
    http_method_names = ['get','post']

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.delete_cookie('sessionid')
        return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_views.index),
    path('accounts/register/', chat_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='chat/logout.html'), name='logout'),
    path('echo/', include('echo.urls')),
    path('chat/', include('chat.urls')),
]
