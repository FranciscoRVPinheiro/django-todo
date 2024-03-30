from .models import Task, User
from rest_framework import serializers

class BaseTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'completed', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']

        # extra_kwargs = {
        #     'title': {'required': True},
        #     'completed': {'required': True},
        # }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'