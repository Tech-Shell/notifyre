from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tasks.models import Task
from django.core.mail import send_mail


def index(request):
    return render(request, 'pages/home.html')


def emailsender(request):
    all_users = User.objects.all()
    for user in all_users:
        try:
            opts_important = user.customer.opts_important
        except:
            opts_important = False
        
        if opts_important == False:
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
            if int(gummy) == 0:
                print('e')
            else:
                send_mail(
                        '[Notifyre] Hourly Mail Notification For\t' + username,
                        new_starting_word +'\nYou currently have '+ gummy + 'tasks left to do. Check the dashboard for more details. Hope you complete them soon ! If you want to get notifications regarding only important tasks then change the setting in the dashboard. Follow this link to the dashboard: http://www.notifyre.tech/accounts/login',
                        'techshell.noreply@gmail.com',
                        [uemail],
                        fail_silently=False 
                    )
        elif opts_important == True:
            user_tasks = Task.objects.filter(user_id = user.id, task_status=False,is_important=True)
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
            if int(gummy) == 0:
                print('e')
            else:
                send_mail(
                        '[Notifyre] Hourly Mail Notification For\t' + username,
                        new_starting_word +'\nYou currently have '+ gummy + 'important tasks left to do. Check the dashboard for more details. Hope you complete them soon ! Follow this link to the dashboard: http://www.notifyre.tech/accounts/login',
                        'techshell.noreply@gmail.com',
                        [uemail],
                        fail_silently=False 
                    )
        else:
            print('Eror')
        



    return redirect('index')