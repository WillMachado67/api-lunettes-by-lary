from rest_framework import serializers

from image_admin.models import ImageProduct
from products.models import Details, Product


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ['image_1', 'image_2', 'image_3',]


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'accessories', 'bridge', 'front', 'hast', 'height', 'lens',
            'material', 'size', 'warranty',
        ]


class ProductsSerializer(serializers.ModelSerializer):
    details = DetailsSerializer()
    imageproduct = ImageProductSerializer()

    class Meta:
        model = Product
        fields = [
            'product_name', 'imageproduct', 'code', 'description', 'category',
            'subcategory', 'value', 'discount', 'price', 'details',
            'related_products',
        ]

    category = serializers.StringRelatedField(
        read_only=True,
    )
    subcategory = serializers.StringRelatedField(
        read_only=True,
    )
