from django.contrib.auth.models import User
from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=200,default="")
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
