from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers
User = get_user_model()

class SignUpAPIView(APIView):
    """
    API View для регистрации пользователя
    """
    def post(self, request):
        

        serializer = serializers.SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_active = True
        user.save()
        
        refresh = RefreshToken.for_user(user)
        response = Response(
            {
                'message': 'вы успешно авторизовались',
                'refresh_token': str(refresh),
                'acees_token': str(refresh.access_token)
            },
            status=status.HTTP_200_OK
        )
        response.set_cookie(
                'refresh_token',
                str(refresh),
                httponly=True, 
                secure=True,
                samesite='Strict'
            )
        response.set_cookie(
                'acseess_token',
                str(refresh.access_token),
                httponly=True, 
                secure=True,
                samesite='Strict'
            )
        
        return response
 


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        tg_id = request.data.get('tg_id')
        password = request.data.get('password')
        name = request.data.get('name')
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(tg_id=tg_id)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            response = Response(
                {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                },
                status=status.HTTP_200_OK
            )

            response.set_cookie(
                'refresh_token',
                str(refresh),
                httponly=True, 
                secure=True,
                samesite='Strict'
            )
            response.set_cookie(
                    'acseess_token',
                    str(refresh.access_token),
                    httponly=True, 
                    secure=True,
                    samesite='Strict'
                )
            
            return response

            
        return Response(
            {'detail': 'Неверные учетные данные.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
        
        
class RefreshTokenAPIView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            
            user_id = token.payload.get('user_id')
            user = User.objects.get(id=user_id)
            refresh = RefreshToken.for_user(user)

            response = Response(
                {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                },
                status=status.HTTP_200_OK
            )
            response.set_cookie(
                'refresh_token',
                str(refresh),
                httponly=True, 
                secure=True,
                samesite='Strict'
            )
            response.set_cookie(
                    'acseess_token',
                    str(refresh.access_token),
                    httponly=True, 
                    secure=True,
                    samesite='Strict'
                )

            return response
        
        except:

            return Response(
            {'detail': 'Токен не валиден'},
            status=status.HTTP_400_BAD_REQUEST
        )

# class CreateApiKeyAPIView(APIView):
#     def get(self, request):
  
#         try:
#             user = request.user
#             try:
#                 apikey = get_object_or_404(ApiKey, user=user)

#                 return Response(
#                     {
#                         'message': 'вы уже создали apikey',
#                         'apikey': apikey.key
#                     },
#                     status=status.HTTP_200_OK
#                 )
#             except:
                
#                 serializer = serializers.ApiKeySerializer().create(user=user)
                
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except:
#             return Response({'message': 'вы должны быть авторизованны'}, status=status.HTTP_400_BAD_REQUEST)