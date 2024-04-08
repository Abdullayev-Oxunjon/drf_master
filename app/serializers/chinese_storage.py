from rest_framework import serializers

from app.models import ChineseStorage


class ChineseStorageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChineseStorage
        fields = ['trek_code', 'product_title', 'product_count', 'product_weight', 'box', 'client_keyword', 'party',
                  'created_at']
        extra_kwargs = {"trek_code": {"read_only": True}}
