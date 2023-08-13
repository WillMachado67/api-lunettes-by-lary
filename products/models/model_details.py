from django.db import models
from django.utils.translation import gettext_lazy as _


class Details(models.Model):
    products = models.OneToOneField(
        'Product', on_delete=models.CASCADE,
    )
    accessories = models.CharField(
        max_length=150, blank=True, verbose_name=_('Accessories')
    )
    bridge = models.FloatField(verbose_name=_('Bridge'))
    front = models.FloatField(verbose_name=_('Front'))
    hast = models.FloatField(verbose_name=_('Hast'))
    height = models.FloatField(verbose_name=_('Height'))
    lens = models.CharField(max_length=32, verbose_name=_('Lens'))
    material = models.CharField(max_length=32, verbose_name=_('Material'))
    size = models.CharField(max_length=32, verbose_name=_('Size'))
    warranty = models.IntegerField(verbose_name=_('Warranty'))

    class Meta:
        verbose_name = _('Detail')
        verbose_name_plural = _('Details')
