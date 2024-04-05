from django.contrib import admin
from django.urls import path
from .views import CreateTask, ListTasks, TaskDetail, UpdateTask, DeleteTask, ListUsers, DeleteUser, UpdateUser, ListTags, CreateTag
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/v1/list-users/', ListUsers.as_view()),
    path('api/v1/update-user/<int:pk>', UpdateUser.as_view()),
    path('api/v1/delete-user/<int:pk>', DeleteUser.as_view()),
    path('api/v1/list/', ListTasks.as_view()),
    path('api/v1/create/', CreateTask.as_view()),
    path('api/v1/detail/<int:pk>', TaskDetail.as_view()),
    path('api/v1/update/<int:pk>', UpdateTask.as_view()),
    path('api/v1/delete/<int:pk>', DeleteTask.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api/v1/list-tags/', ListTags.as_view()),
    path('api/v1/create-tag/', CreateTag.as_view()),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 