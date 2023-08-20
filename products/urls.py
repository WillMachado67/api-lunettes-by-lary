from django.urls import include, path
from rest_framework.routers import SimpleRouter

from products import api, views

app_name = 'products'

products_api_v1_router = SimpleRouter()
products_api_v1_router.register(
    'products',
    api.ProductsApiv1ViewSet,
    basename='product-api',
)

new_colletion_api_v1_router = SimpleRouter()
new_colletion_api_v1_router.register(
    'new_collection',
    api.NewCollectionApiv1ViewSet,
    basename='new-collection-api',
)

feactured_products_api_v1_router = SimpleRouter()
feactured_products_api_v1_router.register(
    'featured_products',
    api.FeaturedProductsApiv1ViewSet,
    basename='featured-products-api',
)


urlpatterns = [
    path('', views.home, name='home'),
    path('get_subcategories', views.get_subcategories, name='get_subcategories'),
    path('', include(products_api_v1_router.urls)),
    path('', include(new_colletion_api_v1_router.urls)),
    path('', include(feactured_products_api_v1_router.urls))
]
