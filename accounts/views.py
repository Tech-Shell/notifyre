from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from tasks.models import Task
import random
from django.core.mail import send_mail

def register(request):
    if request.method == "POST":
        # Get form values
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
                return redirect('index')

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
    if User.is_authenticated:
        if request.user.id == None:
            return redirect('login')
        
        user_tasks = Task.objects.filter(user_id = request.user.id).order_by('-creation_date')
        
        
        context = {
            'tasks':user_tasks,
        }

        return render(request, 'accounts/dashboard.html', context)
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('index')

def reset_email(request):
    if request.method == 'POST':
       user_email = request.POST['user_email']

    context = {
        'user_email':user_email,
    }
    return render(request, 'accounts/reset_email.html', context)

def resets(request):
    if request.method == 'POST':
       new_email = request.POST['new_email']
       user_email = request.POST['user_email']

    current_user = User.objects.get(username=user_email)

    current_user.username = new_email
    current_user.email = new_email
    current_user.save(update_fields=["username","email"]) 
    return redirect('dashboard')




    
    

    