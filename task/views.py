from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, CustomUserCreationForm
# from .helper import taskSearch


# Create your views here.

def userLogin(request):
    page = 'login'
    context = {"page": page}
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        # query the db to check if username exist
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            messages.error(request, "User does not exist")

        # if user exist, authenticate it, then log it in
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('')
        else:
            messages.error(request, "Username and/or password is incorrect")

    return render(request,"task/login_register.html", context)



def userLogout(request):
    page = 'logout'
    context = {'page': page}
    logout(request)
    return render(request, "task/logout.html", context)

    
def register(request):
    page = 'register'
    form = CustomUserCreationForm(request.POST)

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created successfully!")

            login(request, user)
            return redirect('')
    context = {"page": page, "form": form}
    return render(request, "task/login_register.html", context)


@login_required(login_url='login')
def home(request):
    page = 'home'

    user = request.user
    tasks = user.task_set.all()
    context = {"page": page, "tasks": tasks}
    
    # try:
    #     search_query, tasks = taskSearch(request)
    #     context = {"page": page, "tasks": tasks, "search_query": search_query}

    # except:
    #     user = request.user
    #     tasks = user.task_set.all()
    #     context = {"page": page, "tasks": tasks}


    return render(request,"task/home.html", context)



@login_required(login_url='login')
def createTask(request):
    page = "create"
    user = request.user
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user = user
            task.save()
            messages.success(request, 'Task was added successfully!')
            return redirect('')
        
    context = {'form': form, "page": page}
    return render(request, 'task/task_form.html', context)



@login_required(login_url='login')    
def viewTask(request, pk):
    user = request.user
    task = user.task_set.get(id=pk)
    form = TaskForm(instance=task)
    context = {"form":form}
    return render(request, 'task/task_form.html', context)
    


@login_required(login_url='login')
def updateTask(request, pk):
    page = "create"
    user = request.user
    task = user.task_set.get(id=pk)
    # need to instantiate the class TaskForm with the particular task(which we queried using its id) first  
    form = TaskForm(instance=task)

    if request.method == "POST":
        # pass in request.FILE into the form's constructor, which bound the file data to the form
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save()
            #TODO: add success message
            messages.success(request, "Task was updated!")
            # redirect to homepage
            return redirect('/')
        
    context = {"form": form, "page": page}
    return render(request, 'task/update_form.html', context)



@login_required(login_url='login')    
def deleteTask(request, pk):

    page='delete'
    user = request.user
    task = user.task_set.get(id=pk)
    if request.method == "POST":
        # deleting the task object
        task.delete()
        messages.success(request, "Task was deleted!")
        return redirect("/")
    context = {"task": task, "page": page}
    return render(request, "task/delete_confirm.html", context)



