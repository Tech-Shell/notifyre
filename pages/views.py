from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail


def index(request):
    return render(request, 'pages/home.html')



