from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductsSerializer


class ProductsApiV1Base(ModelViewSet):
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class ProductsApiv1ViewSet(ProductsApiV1Base):
    queryset = Product.objects.get_published()


class NewCollectionApiv1ViewSet(ProductsApiV1Base):
    queryset = Product.objects.get_new_collection()


class FeaturedProductsApiv1ViewSet(ProductsApiV1Base):
    queryset = Product.objects.get_featured_products()
