from django.urls import path

from app.views import like_product, unlike_product

urlpatterns = [
    # ... other paths ...
    path('products/<int:product_id>/like/', like_product, name='like-product'),
    path('products/<int:product_id>/unlike/', unlike_product, name='unlike-product'),
]