from django.urls import include, path
from rest_framework.routers import SimpleRouter

from products import views

app_name = 'products'

products_api_v1_router = SimpleRouter()
products_api_v1_router.register(
    'products/api/v1',
    views.ProductsApiv1ViewSet,
    basename='products',
)

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(products_api_v1_router.urls))
]
