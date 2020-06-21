from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tasks.models import Task
from django.core.mail import send_mail


def index(request):
    return render(request, 'pages/home.html')


def emailsender(request):
    all_users = User.objects.all()
    
    for user in all_users:
        user_tasks = Task.objects.filter(user_id = user.id, task_status=False)
        gummy = 0
        for task in user_tasks:
            gummy = gummy + 1
        
        username = user.first_name
        username = str(username)
        username = username.rjust(3)
        uemail = user.email
        gummy = str(gummy)
        gummy = gummy.ljust(2)
        starting_word = f'Hi'
        new_starting_word = starting_word.ljust(2)
        print(f'{username}----{uemail}---{gummy}')
        if gummy == 0:
            send_mail(
                    '[Notifyre] Hourly Mail Notification For\t' + username,
                    new_starting_word +'\nYou currently have '+ gummy + 'tasks left to do. Congratulations on completing all of your tasks ! If you want to add more tasks follow this link to the dashboard: www.notifyre.tech/accounts/dashboard',
                    'techshell.noreply@gmail.com',
                    [uemail],
                    fail_silently=False 
                )
        else:
            send_mail(
                    '[Notifyre] Hourly Mail Notification For\t' + username,
                    new_starting_word +'\nYou currently have '+ gummy + 'tasks left to do. Check the dashboard for more details. Hope you complete them soon ! Follow this link to the dashboard: www.notifyre.tech/accounts/dashboard',
                    'techshell.noreply@gmail.com',
                    [uemail],
                    fail_silently=False 
                )


    return redirect('index')