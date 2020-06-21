from django.urls import path
from . import views

secret_code = '582154151155112851536' 

urlpatterns = [
    path('', views.index, name="index"),
    path(secret_code, views.emailsender, name="emailsender"),
]