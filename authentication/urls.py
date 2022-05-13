from django.urls import path
from .views import RegisterView, VerifyEmail,LoginAPIView,PasswordTokenCheckAPIView,RequestPasswordResetEmail,SetNewPasswordAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('email_verify/',VerifyEmail.as_view(),name='email-verify'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('request_reset_email/',RequestPasswordResetEmail.as_view(),name='request_reset_email'),
    path('password_reset/<uidb64>/<token>',PasswordTokenCheckAPIView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',SetNewPasswordAPIView.as_view(),name='password_reset_complete'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]