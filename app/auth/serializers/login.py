from django.core.validators import RegexValidator
from rest_framework import serializers

from app.models import User


class LoginSerializer(serializers.ModelSerializer):
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = serializers.CharField(
        max_length=25,
        validators=[phone_validator]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', "password"]