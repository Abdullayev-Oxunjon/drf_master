"""
Module: views.py
Description: This module contains views for handling user login requests using Django Rest Framework.

Classes:
    LoginAPIView: API view for user login.

Usage:
    This view is used to handle user login requests. It receives username and password in the request body, validates
    them using a serializer, and generates JWT tokens upon successful authentication.

Example:
    # In urls.py or elsewhere
    from django.urls import path
    from app.views import LoginAPIView

    urlpatterns = [
        path('login/', LoginAPIView.as_view(), name='login'),
    ]
"""
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import Client
from app.serializers import LoginModelSerializer, RequestModelSerializer


class LoginAPIView(APIView):
    """
    API view for user login.
    """

    @swagger_auto_schema(
        request_body=LoginModelSerializer,
        responses={
            status.HTTP_200_OK: "Login successful",
            status.HTTP_400_BAD_REQUEST: "Invalid credentials"
        }
    )
    def post(self, request):
        """
        Handles POST requests for user login.

        Args:
            request (HttpRequest): The HTTP request object containing user login credentials.

        Returns:
            Response: HTTP response with login status and JWT tokens.
        """
        serializer = LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response(data={"message": "Successful login",
                                  'access_token': access_token,
                                  'refresh_token': refresh_token},
                            status=status.HTTP_200_OK)
        return Response(data={"message": "Incorrect credentials"},
                        status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------------------------------------------------------------


class LeaveRequestView(CreateAPIView):
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


class ListRequestView(ListAPIView):
    """
        API view for list requests.

        Attributes:
            serializer_class (class): The serializer class used for serializing/deserializing data.
            queryset (QuerySet): The queryset of client objects used by this view.
            """
    serializer_class = RequestModelSerializer
    queryset = Client.objects.all()

    # Only allow authenticated users to access this view
    permission_classes = [IsAuthenticated]

    # ordering and filtering and search
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ["keyword", "given_time", "fullname", "telegram_id"]
    search_fields = ["keyword", "given_time", "fullname", "telegram_id"]
    ordering_fields = ["given_time", "fullname"]

    @swagger_auto_schema(

        responses={
            status.HTTP_200_OK: "Requests retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid request data"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# -----------------------------------------------------------------------------------------------------

class GetRequestView(RetrieveAPIView):
    """
        API view for get request.

        Attributes:
            serializer_class (class): The serializer class used for serializing/deserializing data.
            queryset (QuerySet): The queryset of client objects used by this view.
    """
    serializer_class = RequestModelSerializer
    queryset = Client.objects.all()
    # Only allow authenticated users to access this view
    permission_classes = [IsAuthenticated]

    # ordering and filtering and search
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]
    filterset_fields = ["keyword", "given_time", "fullname", "telegram_id"]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Request retrieved successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid request data"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# -----------------------------------------------------------------------------------------------------


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


class DeleteRequestView(DestroyAPIView):
    """
           API view for delete request.

           Attributes:
               serializer_class (class): The serializer class used for serializing/deserializing data.
               queryset (QuerySet): The queryset of client objects used by this view.
       """
    serializer_class = RequestModelSerializer
    queryset = Client.objects.all()
    # Only allow authenticated users to access this view

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Request deleted successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid request data"
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# -----------------------------------------------------------------------------------------------------
