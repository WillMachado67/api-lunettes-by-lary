from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product

from .base_model import BaseImageMIxin

verbose_name_base = _('Name')
verbose_name_desktop = _('Image Desktop')
verbose_name_mobile = _('Image Mobile')


class Banner(BaseImageMIxin, models.Model):
    name = models.CharField(
        max_length=25,
        default=_('Image Banner'),
        verbose_name=verbose_name_base,
    )
    image_desktop = models.ImageField(
        upload_to='cover/desktop/banner',
        verbose_name=verbose_name_desktop,
    )
    image_mobile = models.ImageField(
        null=True,
        upload_to='cover/mobile/banner',
        verbose_name=verbose_name_mobile,
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        saved = super().save(*args, **kwargs)

        if self.image_desktop:
            try:
                self.resize_image(self.image_desktop, new_width=1200)
            except FileNotFoundError:
                ...

        if self.image_mobile:
            try:
                self.resize_image(self.image_mobile, new_width=740)
            except FileNotFoundError:
                ...

        return saved


class PersonalizedService(BaseImageMIxin, models.Model):
    name = models.CharField(
        max_length=25,
        default='Image Personalized Service',
        verbose_name=verbose_name_base,
    )
    image_desktop = models.ImageField(
        upload_to='cover/desktop/personalized_service',
        verbose_name=verbose_name_desktop,
    )
    image_mobile = models.ImageField(
        null=True,
        upload_to='cover/mobile/personalized_service',
        verbose_name=verbose_name_mobile,
    )

    class Meta:
        verbose_name = _('Personalized Service')
        verbose_name_plural = _('Personalized Services')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        saved = super().save(*args, **kwargs)

        if self.image_desktop:
            try:
                self.resize_image(self.image_desktop, new_width=960)
            except FileNotFoundError:
                ...

        if self.image_mobile:
            try:
                self.resize_image(self.image_mobile, new_width=440)
            except FileNotFoundError:
                ...

        return saved


class ImageProduct(BaseImageMIxin, models.Model):
    related_product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Related Product')
    )
    image_1 = models.ImageField(
        upload_to='cover/product', verbose_name=_('Image 1')
    )
    image_2 = models.ImageField(
        upload_to='cover/product', verbose_name=_('Image 2')
    )
    image_3 = models.ImageField(
        upload_to='cover/product', verbose_name=_('Image 3')
    )

    class Meta:
        verbose_name = _('Image Product')
        verbose_name_plural = _('Image Products')
