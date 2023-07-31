from rest_framework import serializers

from products.models import Details, Product


class DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    detail = DetailsSerializers()

    class Meta:
        model = Product
        fields = '__all__'

    category = serializers.StringRelatedField(
        read_only=True,
    )
    subcategory = serializers.StringRelatedField(
        read_only=True,
    )
