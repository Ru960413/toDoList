from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.getTasks),
    path('tasks/<str:pk>/', views.viewTask),
    path('tasks/delete/<str:pk>/', views.deleteTask),
    path('tasks/update/<str:pk>/', views.updateTask),
    

    # when user log in, it'll generate a token
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # this will refresh the token
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]