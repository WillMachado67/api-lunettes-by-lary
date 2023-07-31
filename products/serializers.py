from rest_framework import serializers

from products.models import Details, Product


class DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'accessories', 'bridge', 'front', 'hast', 'height', 'lens',
            'material', 'size', 'warranty',
        ]


class ProductsSerializer(serializers.ModelSerializer):
    detail = DetailsSerializers()

    class Meta:
        model = Product
        fields = [
            'product_name', 'code', 'description', 'detail', 'category',
            'subcategory', 'price', 'detail',
        ]

    category = serializers.StringRelatedField(
        read_only=True,
    )
    subcategory = serializers.StringRelatedField(
        read_only=True,
    )
