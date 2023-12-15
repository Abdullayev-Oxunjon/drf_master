from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.auth.serializers.login import LoginSerializer


class LoginAPIView(APIView):

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            status.HTTP_200_OK: "Login successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid Credentials",
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            password = serializer.validated_data.get("password")
            user = authenticate(username=phone_number, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "detail": "Successfully login",
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                }, status=status.HTTP_200_OK)

            return Response({"detail": "Invalid phone number or password"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
