from django.contrib import admin
from . models import Villa, Genel, Havuz,Galleryvilla, Aktivite, Restoran, Spa, Food, Meeting, mainslide
from modeltranslation.admin import TranslationAdmin

@admin.register(Villa)
class VillaAdmin(TranslationAdmin):
    list_display = ("name",)
admin.site.register(Genel)
admin.site.register(Havuz)
admin.site.register(Galleryvilla)
admin.site.register(mainslide)
admin.site.register(Aktivite)
admin.site.register(Restoran)
admin.site.register(Spa)
@admin.register(Food)
class FoodAdmin(TranslationAdmin):
    list_display = ("name",)
admin.site.register(Meeting)


# Register your models here.
