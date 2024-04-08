from rest_framework import serializers

from app.models import Client


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
