from django import forms
from django.contrib import admin

from store.models import Details, Product


class DetailsAdmin(admin.StackedInline):
    model = Details


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['price']
    inlines = [DetailsAdmin]
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


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'subcategory': forms.Select(choices=(('v', 'verdadeiro'), ('f', 'falso'))),
        }
