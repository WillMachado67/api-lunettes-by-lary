from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')


class Subcategory(models.Model):
    name = models.CharField(max_length=25, verbose_name=_('Name'))
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Category')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategorys')
