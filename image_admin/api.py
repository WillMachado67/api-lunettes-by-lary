from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from image_admin.models import Banner, PersonalizedService, ImageCarousel
from image_admin.serializers import (BannerSerializer,
                                     PersonalizedServiceSerializer,
                                     ImageCarouselSerializer)


class BaseModelViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes = [IsAuthenticatedOrReadOnly]


class BannerApiV1Base(BaseModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class PersonalizedServiceApiV1Base(BaseModelViewSet):
    serializer_class = PersonalizedServiceSerializer
    queryset = PersonalizedService.objects.all()


class ImageCarouselApiV1Base(BaseModelViewSet):
    serializer_class = ImageCarouselSerializer
    queryset = ImageCarousel.objects.all()
