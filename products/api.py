from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductsSerializer


class ProductsApiv1ViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    http_method_names = ['get']
