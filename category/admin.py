from django.contrib import admin

from .models import Category, Subcategory


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


@admin.register(Category)
class CategoryInline(admin.ModelAdmin):
    inlines = [SubcategoryInline]
