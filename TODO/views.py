from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class TaskModelViewsSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Task.objects.filter(user = self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

