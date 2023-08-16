from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    name = models.CharField(
        max_length=25,
        default=_('Image Banner'),
    )
    image_banner_desktop = models.ImageField(
        upload_to='cover/banner/desktop',
        verbose_name=_('Image Banner Desktop')
    )
    image_banner_mobile = models.ImageField(
        upload_to='cover/banner/mobile',
        null=True,
        verbose_name=_('Image Banner Mobile'),
    )

    def __str__(self):
        return str(self.name)
