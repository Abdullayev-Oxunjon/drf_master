# This is models.py
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='categories',
                              null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to='products')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE,
        related_name='products',
    )
    is_available = models.BooleanField(default=True)
    discount = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class ProductIngredient(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                related_name='product_ingredients')
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.CASCADE,
                                   related_name='product_ingredients')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} - {self.ingredient.title}"


class Variation(models.Model):
    title = models.CharField(max_length=255)
    price_modifier = models.DecimalField(max_digits=6, decimal_places=2)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                related_name='variations')

    def __str__(self):
        return self.title


class ProductVariation(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                related_name='product_variations')
    variation = models.ForeignKey(to=Variation, on_delete=models.CASCADE,
                                  related_name='product_variations')

    def __str__(self):
        return f"{self.product.title} - {self.variation.title}"
