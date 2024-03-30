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
        token = self.request.headers.get('Authorization').split(' ')[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=decoded_token['user_id'])
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        return super().create(request, *args, **kwargs)


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