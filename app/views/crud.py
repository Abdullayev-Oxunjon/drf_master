from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from app.models import Product, Category, ProductVariation, Variation, ProductIngredient, Ingredient
from app.serializers.crud import ProductSerializer, CategorySerializer, ProductVariationSerializer, VariationSerializer, \
    ProductIngredientSerializer


# Category crud views
class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDestroyAPIView(DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# Product crud views
class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Product variation crud views
class VariationCreateAPIView(CreateAPIView):
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()


class VariationListAPIView(ListAPIView):
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()


class VariationRetrieveAPIView(RetrieveAPIView):
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()


class VariationUpdateAPIView(UpdateAPIView):
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()


class VariationDestroyAPIView(DestroyAPIView):
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()


# Product variation crud views

class ProductVariationCreateAPIView(CreateAPIView):
    serializer_class = ProductVariationSerializer
    queryset = ProductVariation.objects.all()


class ProductVariationListAPIView(ListAPIView):
    serializer_class = ProductVariationSerializer
    queryset = ProductVariation.objects.all()


class ProductVariationRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductVariationSerializer
    queryset = ProductVariation.objects.all()


class ProductVariationUpdateAPIView(UpdateAPIView):
    serializer_class = ProductVariationSerializer
    queryset = ProductVariation.objects.all()


class ProductVariationDestroyAPIView(DestroyAPIView):
    serializer_class = ProductVariationSerializer
    queryset = ProductVariation.objects.all()


# Integredient crud views


class IngredientCreateAPIView(CreateAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientListAPIView(ListAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientUpdateAPIView(UpdateAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientDestroyAPIView(DestroyAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = Ingredient.objects.all()


# Product ingredient crud views


class ProductIngredientCreateAPIView(CreateAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = ProductIngredient.objects.all()


class ProductIngredientListAPIView(ListAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = ProductIngredient.objects.all()


class ProductIngredientRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = ProductIngredient.objects.all()


class ProductIngredientUpdateAPIView(UpdateAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = ProductIngredient.objects.all()


class ProductIngredientDestroyAPIView(DestroyAPIView):
    serializer_class = ProductIngredientSerializer
    queryset = ProductIngredient.objects.all()


