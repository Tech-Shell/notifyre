from django.db import models
from datetime import datetime
from datetime import datetime, timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

bre = utc_to_local(datetime.now)

class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    creation_date = models.DateTimeField(default = bre)
    user_id = models.IntegerField(blank = True)
    task_status = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    def __str__(self):
        return self.title