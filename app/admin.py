from django.contrib import admin

from app.models import Like, User, Product

# Register your models here.#


admin.site.register([
    Like,
    User,
    Product
])
