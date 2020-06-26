from django.urls import path
from . import views
import os


# SECRET_CODE = os.environ.get('SECRET_CODE')
SECRET_CODE = '582154151155112851536'
urlpatterns = [
    path('', views.index, name="index"),
    path(SECRET_CODE, views.emailsender, name="emailsender"),
]