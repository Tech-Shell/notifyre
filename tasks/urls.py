from django.urls import path
from . import views

urlpatterns = [
    path('addtask', views.add_task, name="add_task"),
    path('deletetask', views.delete_task, name="delete_task"),
    path('updatetask', views.update_task, name="update_task"),
    path('updatestask', views.updates_task, name="updates_task"),
]