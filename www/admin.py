from django.contrib import admin

from www.models import *


# Register your models here.
@admin.register(ModelComment)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelCompany)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelGame)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelRating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelImageGame)
class ImageGameAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelImageCompany)
class ImageCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelFavorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass