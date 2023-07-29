from django.db import models
from django.utils.translation import gettext_lazy as _

from category.models import Category, Subcategory


class Product(models.Model):
    product_name = models.CharField(
        max_length=25, verbose_name=_('Product Name')
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
        Subcategory,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        limit_choices_to={'category_id': '1'},
        verbose_name=_('Subcategory')
    )
    valor = models.FloatField(verbose_name=_('Valor')+' R$')
    discount = models.IntegerField(blank=True, verbose_name=_('Discont')+' %')
    price = models.FloatField(verbose_name=_('Price'))
    is_new_colection = models.BooleanField(
        default=False, verbose_name=_('New Colection')
    )
    status = models.BooleanField(default=True, verbose_name=_('Status'))

    def __str__(self):
        return self.product_name

    def calculate_price(self):
        if self.discount is not None:
            self.price = self.valor - (self.valor * (self.discount / 100))
        else:
            self.price = self.valor

    def save(self, *args, **kwargs):
        # Calcular o preço antes de salvar o objeto
        self.calculate_price()
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Details(models.Model):
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
    Product = models.OneToOneField(
        Product, on_delete=models.CASCADE, verbose_name=_('Details')
    )

    def __str__(self):
        return self.accessories

    class Meta:
        verbose_name = _('Details')
        verbose_name_plural = _('Details')
