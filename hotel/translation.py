from . models import Villa, Food
from modeltranslation.translator import TranslationOptions,register

@register (Villa)
class VillaTransOptions(TranslationOptions):
    fields = ("bedrooms","info","page_info",)

@register (Food)
class FoodaTransOptions(TranslationOptions):
    fields = ("info",)
    

