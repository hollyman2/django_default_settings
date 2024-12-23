from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import Account # Импортируйте вашу модель пользователя


class MyView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] # Проверка аутентификации

    def get_queryset(self):
        user = self.request.user
        
        return Account.objects.filter(pk=user.pk)

    def list(self, request):
        queryset = self.get_queryset()

        serializer = YourSerializer(queryset, many=True)
        return Response(serializer.data)
