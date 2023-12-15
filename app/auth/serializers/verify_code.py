from rest_framework import serializers

from app.models import User


class VerifyPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', "verification_code"]
        extra_kwargs = {"verification_code": {"write_only": True}}