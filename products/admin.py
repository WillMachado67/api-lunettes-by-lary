from django import forms
from django.contrib import admin

from products.models import Details, Product

# @admin.register(Details)
# class DetailsAdmin(admin.ModelAdmin):
#     ...


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        category_selected = self.instance.category.name
        self.fields['subcategory'].queryset = self.fields['subcategory'].queryset.filter(
            category__name=category_selected
        )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['price']
    form = ProductAdminForm
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
