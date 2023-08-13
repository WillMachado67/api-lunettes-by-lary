from django.urls import include, path
from rest_framework.routers import SimpleRouter

from products import api, views

app_name = 'products'

products_api_v1_router = SimpleRouter()
products_api_v1_router.register(
    'products/api/v1',
    api.ProductsApiv1ViewSet,
    basename='product-api',
)
# print(products_api_v1_router.urls)
urlpatterns = [
    path('', views.home, name='home'),
    path('get_subcategories', views.get_subcategories, name='get_subcategories'),
    path('', include(products_api_v1_router.urls))
]
