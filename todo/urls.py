from django.contrib import admin
from django.urls import path
from .views import CreateTask, ListTasks, TaskDetail, UpdateTask, DeleteTask, ListUsers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/list-users/', ListUsers.as_view()),
    path('api/v1/list/', ListTasks.as_view()),
    path('api/v1/create/', CreateTask.as_view()),
    path('api/v1/detail/<int:pk>', TaskDetail.as_view()),
    path('api/v1/update/<int:pk>', UpdateTask.as_view()),
    path('api/v1/delete/<int:pk>', DeleteTask.as_view()),
    
]