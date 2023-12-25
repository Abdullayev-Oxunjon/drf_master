from rest_framework import serializers

from app.models import Like


class LikeModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
