from rest_framework import serializers

from app.models import UzbekStorage


class UzbekStorageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzbekStorage
        fields = ['client', 'chinese_storage', 'party', 'created_at', 'price', 'status']
        