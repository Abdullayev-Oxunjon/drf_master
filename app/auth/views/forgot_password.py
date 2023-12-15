from datetime import timedelta

from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.auth.serializers.forgot_password import ForgotPasswordModelSerializer, ForgotChangeUserModelSerializer
from app.models import User
from app.utils import genereation_verification_code, send_sms


class ForgotPasswordView(APIView):

    @swagger_auto_schema(
        request_body=ForgotPasswordModelSerializer,
        responses={
            status.HTTP_200_OK: "Parolni tiklash uchun tasdiqlash kodi jo'natildi.",
            status.HTTP_404_NOT_FOUND: "Foydalanuvchi topilmadi.",
        },
    )
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        try:
            user = User.objects.get(phone_number=phone_number)
            expiration_time = timezone.now() + timedelta(minutes=1)
            verification_code = genereation_verification_code()
            user.activation_key_expires = expiration_time
            user.verification_code = verification_code
            user.save()
            # Emailga tasdiqlash kodi jo'natish
            send_sms(message=f"Tasdiqlash kodi : {verification_code}",
                     recipient=phone_number)

            return Response(data={'message': 'Parolni tiklash uchun tasdiqlash kodi jo\'natildi.'},
                            status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'message': 'Foydalanuvchi telefon raqami manzili topilmadi.'},
                            status=status.HTTP_404_NOT_FOUND)


class VerifyForgotPhoneNumberView(APIView):
    serializer_class = ForgotChangeUserModelSerializer

    @swagger_auto_schema(
        request_body=ForgotChangeUserModelSerializer,
        responses={
            status.HTTP_200_OK: "Telefon raqam tasdiqlandi.",
            status.HTTP_400_BAD_REQUEST: "Tasdiqlash kod muddati tugagan yoki noto'g'ri tasdiqlash kod.",
            status.HTTP_404_NOT_FOUND: "Noto'g'ri tasdiqlash kod yoki email.",
        },
    )
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")
        verification_code = request.data.get('verification_code')
        try:
            user = User.objects.get(phone_number=phone_number,
                                    verification_code=verification_code)

            if user.is_active and user.activation_key_expires > timezone.now():
                # Yangi parolni va tasdiqlashni tekshirish
                if new_password != confirm_password:
                    return Response({'message': 'Parol va tasdiqlash mos kelmadi.'},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    user.set_password(new_password)
                    # user.is_active = True
                    user.save()
                    return Response(data={'message': "Telefon raqam tasdiqlandi va parol o'zgardi"},
                                    status=status.HTTP_200_OK)
            elif user.activation_key_expires < timezone.now() or user.verification_code != verification_code:
                return Response({'message': 'Tasdiqlash kod muddati tugagan yoki noto\'g\'ri tasdiqlash kod.'},
                                status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Noto\'g\'ri tasdiqlash kod yoki email.'}, status=status.HTTP_400_BAD_REQUEST)
