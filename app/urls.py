from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from app.views import ProductViewSet

routers = DefaultRouter()
routers.register(prefix='product',
                 viewset=ProductViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
