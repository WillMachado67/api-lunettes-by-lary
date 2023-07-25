from django.contrib import admin

from .models import Category, Subcategory

# @admin.register(Subcategory)
# class SubcategoryInline(admin.ModelAdmin):
#     ...


class SubcategoryInline(admin.TabularInline):
    model = Subcategory


@admin.register(Category)
class CategoryInline(admin.ModelAdmin):
    inlines = [SubcategoryInline]
