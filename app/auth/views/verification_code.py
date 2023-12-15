from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.auth.serializers.verify_code import VerifyPhoneNumberSerializer
from app.models import User


class VerifyPhoneNumberView(CreateAPIView):
    serializer_class = VerifyPhoneNumberSerializer

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        verification_code = request.data.get("verification_code")
        try:
            instance = User.objects.get(phone_number=phone_number,
                                        verification_code=verification_code)
            if not instance.is_active and instance.activation_key_expires > timezone.now():
                instance.is_active = True
                instance.save()
                return Response({'message': 'Bu foydalanuvchi tasdiqlandi.'},
                                status=status.HTTP_200_OK)
            elif instance.is_active:
                return Response({'message': 'Bu foydalanuvchi  allaqachon tasdiqlangan.'},
                                status=status.HTTP_400_BAD_REQUEST)
            elif instance.activation_key_expires < timezone.now() or instance.verification_code != verification_code:
                instance.delete()
                return Response({'message': 'Tasdiqlash kod muddati tugagan yoki noto\'g\'ri tasdiqlash kod.'},
                                status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Noto\'g\'ri tasdiqlash kod yoki phone_number.'},
                            status=status.HTTP_400_BAD_REQUEST)
