from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    name = models.CharField(
        max_length=25,
        default=_('Image Banner'),
    )
    image_banner = models.ImageField(
        upload_to='cover/banner/',
        verbose_name=_('Image Banner')
    )

    def __str__(self):
        return self.name
