from django.contrib import admin

from .models.model_image import Banner, ImageProduct, PersonalizedService


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['name']
    fieldsets = [(None, {'fields': ['name', 'image_desktop', 'image_mobile']})]


@admin.register(PersonalizedService)
class PersonalizedServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['name']
    fieldsets = [(None, {'fields': ['name', 'image_desktop', 'image_mobile']})]


@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    list_display = ['related_product']
