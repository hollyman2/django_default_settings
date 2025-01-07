from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view(), name='signup'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('activate/<uidb64>/<token>/', views.ActivateAccountAPIView.as_view(), name='activate'),
    path('update_tokens/', views.RefreshTokenAPIView.as_view(), name="update_tokens")
]
