"""
This module defines views for retrieving lists and individual instances of UzbekStorage objects.

Endpoints:
1. ListUzbekStorageView: Retrieves a list of UzbekStorage objects.
2. GetUzbekStorageView: Retrieves a specific UzbekStorage object.

Authentication:
Authentication is required for accessing both views. Only authenticated users can access these endpoints.

Dependencies:
- Django REST Framework: for building RESTful APIs.
- drf_yasg: for generating Swagger/OpenAPI documentation.
"""

from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from app.models import UzbekStorage
from app.serializers.uzbek_storage import UzbekStorageModelSerializer


class ListUzbekStorageView(ListAPIView):
    """
    View for listing UzbekStorage objects.

    This view supports filtering, searching, and ordering capabilities.
    """

    serializer_class = UzbekStorageModelSerializer
    queryset = UzbekStorage.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "UzbekStorage retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid UzbekStorage data"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class GetUzbekStorageView(RetrieveAPIView):
    """
    View for retrieving a specific UzbekStorage object.
    """

    serializer_class = UzbekStorageModelSerializer
    queryset = UzbekStorage.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "UzbekStorage retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid UzbekStorage data"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
