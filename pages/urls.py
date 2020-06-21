from django.urls import path
from . import views

code_da_secret = '582154151155112851536' 

urlpatterns = [
    path('', views.index, name="index"),
    path(code_da_secret, views.emailsender, name="emailsender"),
]