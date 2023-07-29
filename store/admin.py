from django.contrib import admin

from store.models import Details, Product


class DetailsAdmin(admin.StackedInline):
    model = Details
    min_num = 1


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
