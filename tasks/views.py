from django.shortcuts import render, redirect
from .models import Task
from dateutil.tz import *

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        user_id = request.POST['user_id']
        try:
            checkboxes = request.POST.getlist('checker')
        except:
            pass
        
        

        task = Task(title = title, description = description, user_id =user_id,)

        task.save()
        local = tzlocal()
        now = task.creation_date.replace(tzinfo = local)
        import pytz
        tz = pytz.timezone('Asia/Kolkata')
        your_now = now.astimezone(tz)
        your_now = str(your_now)
        grey = your_now.split('+')
        nowh = grey[0]
        task.creation_date = nowh
        try:
            if checkboxes != None:
                checkbox = checkboxes[0]
                task.is_important = True
            else:
                task.is_important = False
        except:
            pass
        
        task.save(update_fields=["is_important","creation_date"])

    return redirect('dashboard')

def delete_task(request):
    if request.method == "POST":
        task_id = request.POST['task_id']

        task = Task.objects.get(id=int(task_id))
        task.delete()
        
    return redirect('dashboard')

def update_task(request):
    
    task_id = request.POST['task_id']
    task = Task.objects.get(id=int(task_id))
    
    context = {
        'task_id':task_id,
        'task':task,
    }

    return render(request, 'tasks/update.html', context)

def updates_task(request):
    
    task_id = request.POST['task_id']
    task = Task.objects.get(id=int(task_id))
    title = request.POST['title']
    description = request.POST['description']
    try:
        checkboxes = request.POST.getlist('checker')
        if checkboxes != None:
            checkbox = checkboxes[0]
            task.task_status = True
        else:
            task.task_status = False
    except:
        pass
    
    
    task.title = title
    task.description = description
    task.save(update_fields=["title","description","task_status",]) 
    return redirect('dashboard')
