from django.urls import path

from app.views.crud import CategoryCreateAPIView, CategoryListAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView, \
    CategoryRetrieveAPIView, ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, \
    ProductDestroyAPIView, VariationCreateAPIView, VariationListAPIView, VariationRetrieveAPIView, \
    VariationUpdateAPIView, VariationDestroyAPIView, ProductVariationCreateAPIView, ProductVariationListAPIView, \
    ProductVariationRetrieveAPIView, ProductVariationUpdateAPIView, ProductVariationDestroyAPIView, \
    IngredientCreateAPIView, IngredientListAPIView, IngredientRetrieveAPIView, IngredientUpdateAPIView, \
    IngredientDestroyAPIView, ProductIngredientCreateAPIView, ProductIngredientListAPIView, \
    ProductIngredientRetrieveAPIView, ProductIngredientUpdateAPIView, ProductIngredientDestroyAPIView

urlpatterns = [
    # Category
    path('create_category/', CategoryCreateAPIView.as_view(), name='create_category'),
    path('list_category/', CategoryListAPIView.as_view(), name='list_category'),
    path('get_category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='get_category'),
    path('update_category/<int:pk>/', CategoryUpdateAPIView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', CategoryDestroyAPIView.as_view(), name='delete_category'),

    # Product
    path('create_product/', ProductCreateAPIView.as_view(), name='create_product'),
    path('list_product/', ProductListAPIView.as_view(), name='list_product'),
    path('get_product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='get_product'),
    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDestroyAPIView.as_view(), name='delete_product'),

    # Variation
    path('create_variation/', VariationCreateAPIView.as_view(), name='create_variation'),
    path('list_variation/', VariationListAPIView.as_view(), name='list_variation'),
    path('get_variation/<int:pk>/', VariationRetrieveAPIView.as_view(), name='get_variation'),
    path('update_variation/<int:pk>/', VariationUpdateAPIView.as_view(), name='update_variation'),
    path('delete_variation/<int:pk>/', VariationDestroyAPIView.as_view(), name='delete_variation'),

    # Product Variation
    path('create_product_variation/', ProductVariationCreateAPIView.as_view(), name='create_product_variation'),
    path('list_product_variation/', ProductVariationListAPIView.as_view(), name='list_product_variation'),
    path('get_product_variation/<int:pk>/', ProductVariationRetrieveAPIView.as_view(), name='get_product_variation'),
    path('update_product_variation/<int:pk>/', ProductVariationUpdateAPIView.as_view(), name='update_product_variation'),
    path('delete_product_variation/<int:pk>/', ProductVariationDestroyAPIView.as_view(), name='delete_product_variation'),

    # Ingredient
    path('create_ingredient/', IngredientCreateAPIView.as_view(), name='create_ingredient'),
    path('list_ingredient/', IngredientListAPIView.as_view(), name='list_ingredient'),
    path('get_ingredient/<int:pk>/', IngredientRetrieveAPIView.as_view(), name='get_ingredient'),
    path('update_ingredient/<int:pk>/', IngredientUpdateAPIView.as_view(), name='update_ingredient'),
    path('delete_ingredient/<int:pk>/', IngredientDestroyAPIView.as_view(), name='delete_ingredient'),

    # Product Ingredient
    path('create_product_ingredient/', ProductIngredientCreateAPIView.as_view(), name='create_product_ingredient'),
    path('list_product_ingredient/', ProductIngredientListAPIView.as_view(), name='list_product_ingredient'),
    path('get_product_ingredient/<int:pk>/', ProductIngredientRetrieveAPIView.as_view(), name='get_product_ingredient'),
    path('update_product_ingredient/<int:pk>/', ProductIngredientUpdateAPIView.as_view(), name='update_product_ingredient'),
    path('delete_product_ingredient/<int:pk>/', ProductIngredientDestroyAPIView.as_view(), name='delete_product_ingredient'),


]