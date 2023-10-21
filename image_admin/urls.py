from rest_framework.routers import SimpleRouter

from image_admin import api

app_name = 'image_admin'

image_banner_api_v1_router = SimpleRouter()
image_banner_api_v1_router.register(
    'image/api/v1/banner',
    api.BannerApiV1Base,
    basename='banner-api',
)

image_personalized_service_api_v1_router = SimpleRouter()
image_personalized_service_api_v1_router.register(
    'image/api/v1/personalized_service',
    api.PersonalizedServiceApiV1Base,
    basename='personalized-service-api',
)

image_carousel_api_v1_router = SimpleRouter()
image_carousel_api_v1_router.register(
    'image/api/v1/carousel',
    api.ImageCarouselApiV1Base,
    basename='carousel-api',
)

urlpatterns = []
urlpatterns += image_banner_api_v1_router.urls
urlpatterns += image_personalized_service_api_v1_router.urls
urlpatterns += image_carousel_api_v1_router.urls

print(image_banner_api_v1_router.urls)
