from rest_framework import serializers

from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'code', 'description', 'category',
            'subcategory', 'price',
        ]

    category = serializers.StringRelatedField(
        read_only=True,
    )
    subcategory = serializers.StringRelatedField(
        read_only=True,
    )
