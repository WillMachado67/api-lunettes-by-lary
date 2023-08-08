from django.db import models
from django.utils.translation import gettext_lazy as _

from category.models import Category


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

    class Meta:
        verbose_name = _('Detail')
        verbose_name_plural = _('Details')


class ProductManager(models.Manager):
    def get_published(self):
        return self.filter(status=True).select_related(
            'category', 'subcategory',
        )


class Product(models.Model):
    objects = ProductManager()
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
        'category.Subcategory',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        limit_choices_to={'category__id': 2},
        verbose_name=_('Subcategory')
    )
    valor = models.FloatField(verbose_name=_('Valor')+' R$')
    discount = models.IntegerField(default=0, verbose_name=_('Discont')+' %')
    price = models.FloatField(verbose_name=_('Price'))
    is_new_colection = models.BooleanField(
        default=False, verbose_name=_('New Colection')
    )
    status = models.BooleanField(default=True, verbose_name=_('Status'))
    detail = models.OneToOneField(
        Details, on_delete=models.CASCADE, verbose_name=_('Detail')
    )
    featured_products = models.BooleanField(default=False)

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
