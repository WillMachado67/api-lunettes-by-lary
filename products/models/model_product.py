from django.db import models
from django.utils.translation import gettext_lazy as _

from category.models import Category


class ProductManager(models.Manager):
    def get_published(self):
        return self.filter(status=True).select_related(
            'category', 'subcategory',
        )


class Product(models.Model):
    objects = ProductManager()
    product_name = models.CharField(
        max_length=25, unique=True, verbose_name=_('Product Name')
    )
    code = models.CharField(max_length=25, unique=True, verbose_name=_('Code'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )
    description = models.TextField(verbose_name=_('Description'))
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=False,
        verbose_name=_('Category')
    )
    subcategory = models.ForeignKey(
        'category.Subcategory',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        verbose_name=_('Subcategory')
    )
    value = models.FloatField(verbose_name=_('Value $'))
    discount = models.IntegerField(default=0, verbose_name=_('Discont')+' %')
    price = models.FloatField(blank=True, verbose_name=_('Price'))
    is_new_collection = models.BooleanField(
        default=False, verbose_name=_('New Collection')
    )
    status = models.BooleanField(default=True, verbose_name=_('Status'))
    featured_products = models.BooleanField(
        default=False, verbose_name=_('Featured Products')
    )

    def __str__(self):
        return self.product_name

    def calculate_price(self):
        if self.discount is not None:
            self.price = self.value - (self.value * (self.discount / 100))
        else:
            self.price = self.value

    def save(self, *args, **kwargs):
        self.calculate_price()
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
