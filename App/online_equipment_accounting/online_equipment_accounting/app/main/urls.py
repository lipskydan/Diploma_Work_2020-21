from django.urls import path
from django.conf.urls import url

from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.user_sign_up, name='user_sign_up'),
    path('login', views.user_login, name='user_login'),
    path("logout/", LogoutView.as_view(), name="logout"),
]