from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutModelSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh_token']
        return data

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError(
                'Token is expired or invalid'
            )