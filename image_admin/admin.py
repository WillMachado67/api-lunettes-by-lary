from django.contrib import admin
from django.utils.html import format_html

from .models.model_image import Banner, PersonalizedService


def image_thumbnail(obj, field_name):
    image_field = getattr(obj, field_name)
    if image_field:
        return format_html(
            f'<img src="{image_field.url}" width="50" height="50" />'
        )
    return 'Nenhuma imagem'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_desktop', 'image_mobile']
    readonly_fields = ['name']

    def image_desktop(self, obj):
        return image_thumbnail(obj, 'image_desktop')

    def image_mobile(self, obj):
        return image_thumbnail(obj, 'image_mobile')


@admin.register(PersonalizedService)
class PersonalizedServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_desktop_thumbnail', 'image_mobile_thumbnail']
    readonly_fields = ['name']

    def image_desktop_thumbnail(self, obj):
        return image_thumbnail(obj, 'image_desktop')

    def image_mobile_thumbnail(self, obj):
        return image_thumbnail(obj, 'image_mobile')
