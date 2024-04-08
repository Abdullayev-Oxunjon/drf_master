from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView

from app.models import UzbekStorage
from app.serializers.uzbek_storage import UzbekStorageModelSerializer


class CreateUzbekStorageView(CreateAPIView):
    """
    API view for creating a UzbekStorage.

    Attributes:
        serializer_class (class): The serializer class used for serializing/deserializing data.
        queryset (QuerySet): The queryset of client objects used by this view.
    """

    serializer_class = UzbekStorageModelSerializer
    queryset = UzbekStorage.objects.all()

    @swagger_auto_schema(
        request_body=UzbekStorageModelSerializer,
        responses={status.HTTP_201_CREATED: "UzbekStorage created successfully",
                   status.HTTP_400_BAD_REQUEST: "Invalid UzbekStorage data"}

    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
