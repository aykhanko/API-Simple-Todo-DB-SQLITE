from app.models import Todos
from app.api.serializer import TodosSerializer
from rest_framework import generics
from app.api.permissions import OwnTodoOrReadOnly
from rest_framework.permissions import IsAuthenticated

class TodosList(generics.ListCreateAPIView):
    serializer_class = TodosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todos.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)

class TodosDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodosSerializer
    permission_classes = [OwnTodoOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Todos.objects.filter(user=user)