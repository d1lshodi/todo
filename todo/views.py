from .models import (TodoModel)
from .serializers import (TodoSerializer)
from rest_framework import generics
from .permissions import IsOwnerPermission

class ListCreateTodoView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class DetailUpdateDeleteTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)
