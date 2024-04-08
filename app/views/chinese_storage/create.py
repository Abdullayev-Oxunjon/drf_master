from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView

from app.models import ChineseStorage
from app.serializers.chinese_storage import ChineseStorageModelSerializer


class CreateChineseStorageView(CreateAPIView):
    """
    API view for creating a ChineseStorage.

    Attributes:
        serializer_class (class): The serializer class used for serializing/deserializing data.
        queryset (QuerySet): The queryset of client objects used by this view.
    """

    serializer_class = ChineseStorageModelSerializer
    queryset = ChineseStorage.objects.all()

    @swagger_auto_schema(
        request_body=ChineseStorageModelSerializer,  # Use your serializer class
        responses={
            status.HTTP_201_CREATED: "ChineseStorage created successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid ChineseStorage data"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
