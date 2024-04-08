"""
This module defines views for retrieving and listing ChineseStorage objects.

These views are built on top of Django REST Framework and utilize filters, search, and ordering capabilities.

Endpoints:
1. ChineseStorageListView: Lists ChineseStorage objects.
2. GetChineseStorageView: Retrieves a specific ChineseStorage object.

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

from app.models import ChineseStorage
from app.serializers.chinese_storage import ChineseStorageModelSerializer


class ListChineseStorageView(ListAPIView):
    """
    View for listing ChineseStorage objects.

    This view supports filtering, searching, and ordering capabilities.
    """

    serializer_class = ChineseStorageModelSerializer
    queryset = ChineseStorage.objects.all()

    # Only allow authenticated users to access this view
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['client_keyword__keyword', 'party__title', 'created_at', 'product_title', "box"]
    ordering_fields = ['created_at']
    search_fields = ['client_keyword__keyword', 'party__title', 'created_at', 'product_title', "box", "product_count",
                     "product_weight"]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "ChineseStorage retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid ChineseStorage data"
        }
    )
    def get(self, request, *args, **kwargs):
        """
        Get method to retrieve ChineseStorage objects.

        Returns:
        - Response: HTTP response containing the requested ChineseStorage objects.
        """
        return super().get(request, *args, **kwargs)


class GetChineseStorageView(RetrieveAPIView):
    """
    View for retrieving a specific ChineseStorage object.

    This view supports filtering and searching capabilities.
    """

    serializer_class = ChineseStorageModelSerializer
    queryset = ChineseStorage.objects.all()

    # Only allow authenticated users to access this view
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "ChineseStorage retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid ChineseStorage data"
        }
    )
    def get(self, request, *args, **kwargs):
        """
        Get method to retrieve a specific ChineseStorage object.

        Returns:
        - Response: HTTP response containing the requested ChineseStorage object.
        """
        return super().get(request, *args, **kwargs)
