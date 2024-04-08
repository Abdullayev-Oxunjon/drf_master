"""
Module: views.py
Description: This module contains views for handling user login requests using Django Rest Framework.

Classes:
    LoginAPIView: API view for user login.

Usage:
    This view is used to handle user login requests. It receives username and password in the request body, validates
    them using a serializer, and generates JWT tokens upon successful authentication.

Example:
    # In urls.py or elsewhere
    from django.urls import path
    from app.views import LoginAPIView

    urlpatterns = [
        path('login/', LoginAPIView.as_view(), name='login'),
    ]
"""
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.serializers.login import LoginModelSerializer


class LoginAPIView(APIView):
    """
    API view for user login.
    """

    @swagger_auto_schema(
        request_body=LoginModelSerializer,
        responses={
            status.HTTP_200_OK: "Login successful",
            status.HTTP_400_BAD_REQUEST: "Invalid credentials"
        }
    )
    def post(self, request):
        """
        Handles POST requests for user login.

        Args:
            request (HttpRequest): The HTTP request object containing user login credentials.

        Returns:
            Response: HTTP response with login status and JWT tokens.
        """
        serializer = LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response(data={"message": "Successful login",
                                  'access_token': access_token,
                                  'refresh_token': refresh_token},
                            status=status.HTTP_200_OK)
        return Response(data={"message": "Incorrect credentials"},
                        status=status.HTTP_400_BAD_REQUEST)
