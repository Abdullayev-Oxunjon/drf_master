from datetime import timedelta

from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.auth.serializers.register import RegisterUserSerializer
from app.utils import genereation_verification_code, send_sms


class RegisterView(APIView):
    serializer_class = RegisterUserSerializer

    @swagger_auto_schema(
        request_body=RegisterUserSerializer,
        responses={
            status.HTTP_201_CREATED: "Successfully created",
            status.HTTP_400_BAD_REQUEST: "Invalid Credentials"
        }
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = genereation_verification_code()
            expiration_time = timezone.now() + timedelta(minutes=1)
            serializer.save(verification_code=verification_code, activation_key_expires=expiration_time)
            send_sms(message=f"Tasdiqlash kodi: {verification_code}", recipient=phone_number)
            message = "Tasdiqlash kodi yuborildi. Iltimos SMS orqali tasdiqlab yuboring."
            return Response(data={'message': message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)