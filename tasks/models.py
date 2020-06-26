from django.db import models
from datetime import datetime

class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    creation_date = models.DateTimeField(default = datetime.now)
    user_id = models.IntegerField(blank = True)
    task_status = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    def __str__(self):
        return self.title