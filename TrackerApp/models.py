from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField

#Deadline = Термін виконання (дата)
class Task(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Deadline = models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    objects = None
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"Comment by {self.user} on {self.task}"

# Create your models here.
