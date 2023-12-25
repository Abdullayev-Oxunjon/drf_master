

from .models import Product
from modeltranslation.translator import register, TranslationOptions

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')