from .models import Task, User
from rest_framework import generics
from .serializers import BaseTasksSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner
from django.conf import settings
import jwt

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ListTasks(generics.ListAPIView):
    serializer_class = BaseTasksSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user.id)

class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = BaseTasksSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        token = self.request.auth
        if token is not None:
            user_id = token.user_id
            user = User.objects.get(id=user_id)
            serializer.save(user=user)
            
class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = BaseTasksSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class UpdateTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = BaseTasksSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = BaseTasksSerializer
    permission_classes = [IsAuthenticated, IsOwner]