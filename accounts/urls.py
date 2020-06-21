from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
    path('resetemail', views.reset_email, name="reset_email"),
    path('resets', views.resets, name="resets"),
]