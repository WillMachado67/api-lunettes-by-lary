from rest_framework.viewsets import ModelViewSet

from image_admin.models import Banner, PersonalizedService
from image_admin.serializers import (BannerSerializer,
                                     PersonalizedServiceSerializer)


class BannerApiV1Base(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    http_method_names = ['get']


class PersonalizedServiceApiV1Base(ModelViewSet):
    serializer_class = PersonalizedServiceSerializer
    queryset = PersonalizedService.objects.all()
    http_method_names = ['get']
