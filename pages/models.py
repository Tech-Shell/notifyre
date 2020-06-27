from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    opts_important = models.BooleanField(default=False)
    phone_number = models.CharField(default="N/A", max_length=15)
    def __str__(self):
        return self.user