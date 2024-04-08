from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import Client
from app.serializers.request import RequestModelSerializer


class UpdateRequestView(UpdateAPIView):
    """
           API view for update request.

           Attributes:
               serializer_class (class): The serializer class used for serializing/deserializing data.
               queryset (QuerySet): The queryset of client objects used by this view.
       """
    serializer_class = RequestModelSerializer
    queryset = Client.objects.all()
    # Only allow authenticated users to access this view

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=RequestModelSerializer,
        responses={
            status.HTTP_200_OK: "Request updated successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid request data"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

# -----------------------------------------------------------------------------------------------------
