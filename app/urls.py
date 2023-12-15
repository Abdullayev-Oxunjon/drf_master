from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.auth.views.change_password import ChangePasswordView
from app.auth.views.forgot_password import ForgotPasswordView, VerifyForgotPhoneNumberView
from app.auth.views.login import LoginAPIView
from app.auth.views.logout import LogoutAPIView
from app.auth.views.register import RegisterView
from app.auth.views.verification_code import VerifyPhoneNumberView

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("register-verify/", VerifyPhoneNumberView.as_view(), name='register-verify'),
    path("login/", LoginAPIView.as_view(), name='login'),
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),
    path("forgot-password/", ForgotPasswordView.as_view(), name='forgot-password'),
    path("veriy-forgot-password/", VerifyForgotPhoneNumberView.as_view(), name='verify-forgot-password'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
