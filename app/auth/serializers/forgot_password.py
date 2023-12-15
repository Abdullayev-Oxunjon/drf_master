from rest_framework import serializers

from app.models import User


class ForgotPasswordModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']


class ForgotChangeUserModelSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['phone_number', "new_password", "confirm_password", "verification_code"]
        extra_kwargs = {
            "new_password": {"write_only": True},
            "confirm_password": {"write_only": True},
            "verification_code": {"write_only": True},
        }