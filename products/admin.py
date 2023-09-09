from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from products.models import Details, Product


class DetailsInline(admin.StackedInline):
    model = Details
    extra = 1
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js',
            'admin/js/script.js',
        )

    inlines = [DetailsInline]

    admin_site = admin.AdminSite
    admin_site.site_title = "Lunettes"
    admin_site.site_header = "Lunettes Admin"
    admin_site.index_title = "Dashboard"

    list_display = [
        'product_name',
        'code',
        'category',
        'subcategory',
        'status',
        'price',
    ]
    list_display_links = ['product_name', 'code']
    list_filter = [
        'category',
        'subcategory',
        'status',
        'is_new_collection',
        'featured_products',
    ]
    search_fields = ['product_name', 'code']
    fieldsets = [
        (_('Product Information'), {
            'fields': [
                'product_name',
                'code',
                'category',
                'subcategory',
                'status',
                'is_new_collection',
                'featured_products',
            ],
        }),
        (_('Calculated Price'), {
            'fields': [
                'value',
                'discount',
                'price',
            ],
        }),
        (_('Related Products'), {
            'fields': [
                'related_products',
            ]
        })
    ]
    paginator_per_page = 10
