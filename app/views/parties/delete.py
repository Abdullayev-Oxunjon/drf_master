from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import Party
from app.serializers.parties import PartyModelSerializer


class DeletePartyView(DestroyAPIView):
    """
           API view for delete party.

           Attributes:
               serializer_class (class): The serializer class used for serializing/deserializing data.
               queryset (QuerySet): The queryset of client objects used by this view.
       """
    serializer_class = PartyModelSerializer
    queryset = Party.objects.all()
    # Only allow authenticated users to access this view

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Party deleted successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid party data"
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
