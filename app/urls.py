from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import RegisterApiView, LoginAPIView, ProductModelViewSet

routers = DefaultRouter()
routers.register(prefix='product',
                 viewset=ProductModelViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

]