from .models import Task, User, Tag
from rest_framework import serializers

class BaseTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'tag']

        extra_kwargs = {
            'title': {'required': True},
            'completed': {'required': True}
        }

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'