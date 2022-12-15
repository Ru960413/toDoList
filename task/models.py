from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


# TODO: create task model 
class Task(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    task_name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    # auto_now_add: set the field to now when the object is first created
    creation = models.DateTimeField(auto_now_add=True)
    # allow task to have a blank deadline
    deadline = models.DateField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    #add category DONE
    

    def __str__(self):
        return self.task_name
    
    class Meta:
        ordering = ['category', 'deadline', 'task_name'] 




