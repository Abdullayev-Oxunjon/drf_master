from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product, Cart, Wishlist, CartItem
from .serializers import ProductSerializer, WishlistSerializer, CartItemSerializer, RegisterModelSerializer, \
    LoginModelSerializer


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
            return Response(data={"Message":"User successfully registered"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    @swagger_auto_schema(
        request_body=LoginModelSerializer,
        responses={
            status.HTTP_200_OK:"Login successfully",
            status.HTTP_400_BAD_REQUEST:"Invalid Credentials",
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
            return Response(data={"Message":"Successfully login",
                                  # "token":token.key
                                  'access_token': access_token,
                                  'refresh_token': refresh_token},
                            status=status.HTTP_200_OK)
        return Response(data={serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    quantity = int(request.data.get('quantity', 1))
    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        cart=cart
    )

    cart_item.quantity += cart_item.quantity - 1
    cart_item.quantity = quantity
    cart_item.save()
    return Response(data={"message": "Product added to cart"},
                    status=201)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, product_id):
    cart_item = CartItem.objects.filter(
        cart__user=request.user,
        id=product_id
    ).first()
    if cart_item:
        cart_item.delete()
        message = f'Product removed from cart!'
        return Response(data={"message": message}, status=204)
    else:
        message = f'Product not found in cart!'
        return Response(data={"message": message}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart_items(request):

    cart = Cart.objects.filter(user=request.user).first()
    if cart:

        cart_item_serializer = CartItemSerializer(cart.cartitem_set.all(), many=True)
        cart_total = sum([item.total_price for item in cart.cartitem_set.all()])

        return Response(data={
            "cart_items": cart_item_serializer.data,
            "cart_total": cart_total
        })
    else:
        return Response(data={"cart_items": [],
                              "cart_total": 0}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request, product_id):
    product = get_object_or_404(klass=Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(
        user=request.user,
    )
    wishlist.items.add(product)
    wishlist.save()
    serializer = WishlistSerializer(wishlist)
    return Response(serializer.data,
                    status=201)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.items.remove(product)
    message = f'Product removed from wishlist!'
    return Response(data={"message": message}, status=204)


class WishlistListAPiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return [self.request.user.wishlist]
