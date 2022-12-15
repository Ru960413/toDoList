from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
#TODO: create taskForm, UserCreationForm


# add UserCreationForm for user registration
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'password2': 'confirm_password' 
        }
    
    

# add taskForm for task creation
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'category', 'complete', 'deadline']
        widgets = {
            'deadline': widgets.DateInput(format=('%Y/%m/%d'), attrs={'type':'date'})
        }