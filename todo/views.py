from .models import Task, User, Tag
from rest_framework import generics
from .serializers import BaseTasksSerializer, UserSerializer, TagsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner
from django.conf import settings

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateUser(generics.UpdateAPIView):
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

class ListTags(generics.ListAPIView):
    serializer_class = TagsSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

class CreateTag(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        token = self.request.auth
        if token is not None:
            user_id = token.user_id
            user = User.objects.get(id=user_id)
            serializer.save(user=user)