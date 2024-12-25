from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ToDoItem
from .serializers import ToDoSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

class TodoViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated] 

    def get_serializer_class(self):
        return ToDoSerializer

    def get_queryset(self):
        return ToDoItem.objects.filter(author=self.request.user)

    def get(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data.user == request.user
        print(validated_data.user)
        serializer.create(validated_data=request.data) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        if item.author != request.user:
            raise PermissionDenied("You are not the owner")
        item.delete()
        return Response({"message": "The item has been deleted"})

    def patch(self, request, pk):
        item = get_object_or_404(ToDoItem, pk=pk)
        if item.author != request.user:
            raise PermissionDenied("You are not the owner")
        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

