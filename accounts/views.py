from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        i  = name.split()
        j = i[0]
        if password == password2:
            if User.objects.filter(username = username).exists():
                    messages.success(request,"An account with this email already exists")
                    return redirect('register')
            else:
                user = User.objects.create_user(username = username,
                password = password,first_name=j,email=username)
                user.save()
                auth.login(request, user)
                messages.success(request,"You can now log in.")
                return redirect('login')

        else:
            messages.success(request,'Passwords do not match.')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
        
       user = auth.authenticate(username = username,password = password)

       if user:
          auth.login(request, user)
          return redirect('dashboard')
       else:
            messages.success(request,"Invalid Credentials")
            return redirect('login')       
    else:
        return render(request,'accounts/login.html')

def dashboard(request):
    return redirect('index')
    # return render(request, 'accounts/dashboard.html', context)

