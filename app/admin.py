from django.contrib import admin

from app.models import Product, User, Wishlist, Cart, CartItem

admin.site.register([Product
                     ,User,
                    Wishlist,
                     Cart,
                     CartItem])