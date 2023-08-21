from django.contrib import admin

from .models.model_image import Banner, PersonalizedService


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    readonly_fields = ['name']


@admin.register(PersonalizedService)
class PersonalizedServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['name']
