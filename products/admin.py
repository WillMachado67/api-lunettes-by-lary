from django import forms
from django.contrib import admin

from products.models import Details, Product

# @admin.register(Details)
# class DetailsAdmin(admin.ModelAdmin):
#     ...


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js',
            'admin/js/script.js',
        )
    readonly_fields = ['price']
    list_display = [
        'product_name',
        'code',
        'category',
        'subcategory',
        'status',
        'is_new_colection',
        'price',
    ]
    list_display_links = ['product_name', 'code']
    list_editable = ['status', 'is_new_colection']
    list_filter = ['category', 'subcategory', 'status', 'is_new_colection']
    search_fields = ['product_name', 'code']
