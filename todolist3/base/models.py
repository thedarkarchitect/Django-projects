from django.db import models
from django.contrib.auth.models import User #user class model createed by djang 

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title #this is what is seen by user after task creation

    class Meta:
        ordering = ['complete'] #