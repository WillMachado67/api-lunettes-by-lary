from rest_framework import serializers

from products.models import Details, Product


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'accessories', 'bridge', 'front', 'hast', 'height', 'lens',
            'material', 'size', 'warranty',
        ]


class ProductsSerializer(serializers.ModelSerializer):
    details = DetailsSerializer()

    class Meta:
        model = Product
        fields = [
            'product_name', 'code', 'description', 'category',
            'subcategory', 'value', 'discount', 'price', 'details',
        ]

    category = serializers.StringRelatedField(
        read_only=True,
    )
    subcategory = serializers.StringRelatedField(
        read_only=True,
    )
