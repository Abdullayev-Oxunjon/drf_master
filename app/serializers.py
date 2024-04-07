"""
Module: serializers.py
Description: This module contains a serializer for user login functionality using Django authentication
and Django Rest Framework.

Classes:
    LoginModelSerializer: Serializer class for user login.

Usage:
    This serializer is used to handle user login requests. It validates the provided username and password, authenticates
    the user using Django's authentication system, and raises validation errors if the credentials are invalid.

Example:
    # In views.py or elsewhere
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from app.serializers import LoginModelSerializer

    class LoginView(APIView):
        def post(self, request):
            serializer = LoginModelSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data['user']
                # Perform further actions with the authenticated user
                return Response({"message": "Login successful", "user_id": user.id})
            else:
                return Response(serializer.errors, status=400)
"""

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import User, Client


class LoginModelSerializer(serializers.ModelSerializer):
    """
    Serializer class for user login.
    """

    username = serializers.CharField(max_length=60)
    password = serializers.CharField(max_length=155)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        """
        Validates the username and password provided for login.

        Args:
            data (dict): The input data containing username and password.

        Returns:
            dict: The validated data with the authenticated user added.

        Raises:
            ValidationError: If the username or password is missing, or if the credentials are invalid.
        """
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError("Invalid username or password")
        else:
            raise ValidationError("Both username and password are required")

        data['user'] = user
        return data


# -----------------------------------------------------------------------------------------------------


class RequestModelSerializer(serializers.ModelSerializer):
    """
    Serializer for handling leave request model.

    Attributes:
        fullname (str): The full name of the client.
        telegram_id (str): The Telegram ID of the client.

    Meta:
        model (Client): The model class associated with this serializer.
        fields (list): The fields to include in the serialized representation.
        extra_kwargs (dict): Extra keyword arguments to customize field behavior.
    """

    class Meta:
        """
        Metadata class for the serializer.
        """
        model = Client
        fields = ["fullname", "telegram_id", "keyword", "given_time"]
        extra_kwargs = {"keyword": {"read_only": True},
                        "given_time": {"read_only": True}}

# -----------------------------------------------------------------------------------------------------
