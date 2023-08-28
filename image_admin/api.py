from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from image_admin.models import Banner, PersonalizedService
from image_admin.serializers import (BannerSerializer,
                                     PersonalizedServiceSerializer)


class BaseModelViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]


class BannerApiV1Base(BaseModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class PersonalizedServiceApiV1Base(BaseModelViewSet):
    serializer_class = PersonalizedServiceSerializer
    queryset = PersonalizedService.objects.all()
