from rest_framework import serializers

from app.models import User


class ChangeUserModelSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=55)

    class Meta:
        model = User
        fields = ['password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True},
                        'confirm_password': {'write_only': True}}