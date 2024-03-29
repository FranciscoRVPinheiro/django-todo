from .models import Task, User
from rest_framework import serializers

class BaseTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'