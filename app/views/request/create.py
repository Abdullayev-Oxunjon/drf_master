from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView

from app.models import Client
from app.serializers.request import RequestModelSerializer


class CreateRequestView(CreateAPIView):
    """
        API view for creating  request.

        Attributes:
            serializer_class (class): The serializer class used for serializing/deserializing data.
            queryset (QuerySet): The queryset of client objects used by this view.
        """

    serializer_class = RequestModelSerializer
    queryset = Client.objects.all()

    @swagger_auto_schema(
        request_body=RequestModelSerializer,
        responses={
            status.HTTP_201_CREATED: "Request created successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid request data"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# -----------------------------------------------------------------------------------------------------
