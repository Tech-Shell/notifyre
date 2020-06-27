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
    path('optsimportant', views.opts_important, name="opts_important"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/email_input.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/vercode.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/new_final_message.html"), name="password_reset_complete"),

]