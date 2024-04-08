from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView

from app.models import Party
from app.serializers.parties import PartyModelSerializer


class CreatePartyView(CreateAPIView):
    """
    API view for creating a party.

    Attributes:
        serializer_class (class): The serializer class used for serializing/deserializing data.
        queryset (QuerySet): The queryset of client objects used by this view.
    """

    serializer_class = PartyModelSerializer
    queryset = Party.objects.all()

    @swagger_auto_schema(
        request_body=PartyModelSerializer,  # Use your serializer class
        responses={
            status.HTTP_201_CREATED: "Party created successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid party data"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)