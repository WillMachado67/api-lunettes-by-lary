from rest_framework.serializers import ModelSerializer

from image_admin.models import Banner, PersonalizedService, ImageCarousel


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ['name', 'image_desktop', 'image_mobile']


class PersonalizedServiceSerializer(ModelSerializer):
    class Meta:
        model = PersonalizedService
        fields = ['name', 'image_desktop', 'image_mobile']


class ImageCarouselSerializer(ModelSerializer):
    class Meta:
        model = ImageCarousel
        fields = ['name', 'image_carousel']
