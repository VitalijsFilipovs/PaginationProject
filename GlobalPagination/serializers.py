from rest_framework import serializers
from .models import Task  # <-- Важно! Импорт настоящей модели

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']
