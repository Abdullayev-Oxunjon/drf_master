from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.auth.serializers.change_password import ChangeUserModelSerializer


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        request_body=ChangeUserModelSerializer,  # Use your serializer here
        responses={
            200: 'Password successfully changed',
            400: 'Bad Request',
            401: 'Unauthorized',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = ChangeUserModelSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']

            # Yangi parolni saqlash
            user = request.user
            user.set_password(password)
            user.save()

            return Response({'message': 'Parol muvaffaqiyatli o\'zgartirildi'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
