from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet

from products.models import Product


def home(request):
    return redirect('admin/')


class ProductsApiv1ViewSet(ModelViewSet):
    queryset = Product.objects.all()
