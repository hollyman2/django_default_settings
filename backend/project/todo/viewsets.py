from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ToDoItem
from .serializers import ToDoSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

class TodoViewset(generics.GenericAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     pass
    # def get_serializer_class(self):
    #     pass
    def list(self, request):
        items = get_list_or_404(ToDoItem, author=self.user)
        data = ToDoSerializer(items, many=True)
        
        return Response(
            {'data': data},
            status=status.HTTP_200_OK
        )

    def delete(self, request, id):
        item = get_object_or_404(ToDoItem, id=id)
        post_serializer = ToDoSerializer(item)
        if request.user == post_serializer.data.get('author'):
            item.delete()

            return Response(
                {'message': 'The item has been deleted'},
                status=status.HTTP_200_OK,
            )
        
        else:

            return Response(
                {'error': 'You are not the owner'},
                status=status.HTTP_400_BAD_REQUEST
            )


    def create(self, request, *args, **kwargs):

        data = ToDoSerializer().create(
            user = request.user,
            validated_data = request.data
        )

        return Response(
            {'item': data},
            status=status.HTTP_201_CREATED
        )

    def patch(self, request, *args, id):

        item = get_object_or_404(ToDoItem, id=id)
        post_serializer = ToDoSerializer(item)
        if request.user == post_serializer.data.get('author'):
            data = ToDoSerializer().edit(
            item = item,
            validated_data = request.data
            )

            return Response(
                {'data': data},
                status=status.HTTP_200_OK
            )
        
        else:

            return Response(
                {'error': 'You are not the owner'},
                status=status.HTTP_400_BAD_REQUEST
            )

        
