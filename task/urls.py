from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=""),
    path('login/',views.userLogin, name="login"),
    path('logout/',views.userLogout, name="logout"),
    path('register/',views.register, name="register"),
    path('create-task', views.createTask, name="create-task"),
    path('view-task/<str:pk>/', views.viewTask, name="view-task"),
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
    
]
