from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    deadlines = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
