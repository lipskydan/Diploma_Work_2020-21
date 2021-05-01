from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.user_sign_up, name='user_sign_up'),
    path('login', views.user_login, name='user_login'),
    path("logout/", LogoutView.as_view(), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)