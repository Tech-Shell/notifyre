from django.urls import path
from . import views
import os


SECRET_CODE = os.environ.get('SECRET_CODE')

urlpatterns = [
    path('', views.index, name="index"),
    path(SECRET_CODE, views.emailsender, name="emailsender"),
]