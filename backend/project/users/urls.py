from django.urls import path
from . import views

app_name = 'accounts_api'

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view(), name='signup'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('update_tokens/', views.RefreshTokenAPIView.as_view(), name="update_tokens")
]
