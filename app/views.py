from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import Product
from app.permission import  IsAdminOrReadOnly
from app.serializers import ProductModelSerializer, RegisterModelSerializer, LoginModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminOrReadOnly]


class RegisterApiView(APIView):

    @swagger_auto_schema(
        request_body=RegisterModelSerializer,
        responses={
            status.HTTP_201_CREATED: "User registered successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid input",
        }
    )
    def post(self, request):
        serializer = RegisterModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"Message": "User successfully registered"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    @swagger_auto_schema(
        request_body=LoginModelSerializer,
        responses={
            status.HTTP_200_OK: "Login successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid Credentials",
        }
    )
    def post(self, request):
        serializer = LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            # token, created = Token.objects.get_or_create(user=user)
            return Response(data={"Message": "Successfully login",
                                  # "token":token.key
                                  'access_token': access_token,
                                  'refresh_token': refresh_token},
                            status=status.HTTP_200_OK)
        return Response(data={serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
