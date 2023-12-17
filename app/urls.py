from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.views import ProductViewSet, add_to_cart, get_cart_items, remove_from_cart, add_to_wishlist, \
    remove_from_wishlist, get_wishlist, RegisterApiView, LoginAPIView, CartListApiView

routers = routers.DefaultRouter()
routers.register(prefix="product",
                 viewset=ProductViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('add_to_cart/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('get_cart_items/', get_cart_items, name="get_cart_items"),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name="remove_from_cart"),
    path('cart/', CartListApiView.as_view(), name="cart"),

    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name="add_to_wishlist"),
    path('remove_from_wishlist/<int:product_id>/', remove_from_wishlist, name="remove_from_wishlist"),
    path('get_wishlist/', get_wishlist, name="get_wishlist"),

    path('register/', RegisterApiView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
