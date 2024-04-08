from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from app.models import Party
from app.serializers.parties import PartyModelSerializer


class ListPartyView(ListAPIView):
    serializer_class = PartyModelSerializer
    queryset = Party.objects.all()
    #     # Only allow authenticated users to access this view

    permission_classes = [IsAuthenticated]
    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend
    ]

    filterset_fields = ["title", "created_at"]
    ordering_fields = ["created_at"]
    search_fields = ["title", "created_at"]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Parties retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid party data"

        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# -----------------------------------------------------------------------------------------------------


class GetPartyView(RetrieveAPIView):
    serializer_class = PartyModelSerializer
    queryset = Party.objects.all()
    # Only allow authenticated users to access this view
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Party retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid party data"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
