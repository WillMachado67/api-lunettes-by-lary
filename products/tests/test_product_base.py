from category.models import Category, Subcategory
from products.models import Product


class ProductMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_subcategory(self, category, name='Subcategory'):
        return Subcategory.objects.create(category=category, name=name)

    def make_product(
        self,
        category_data=None,
        subcategory_data=None,
        product_name='Glass',
        code='123',
        description='Description of the product',
        valor=100.00,
        discount=10,
        price=100.00,
        is_new_colection=False,
        status=True,
    ):
        if category_data is None:
            category_data = {}

        if subcategory_data is None:
            subcategory_data = {}

        return Product.objects.create(
            category=self.make_category(**category_data),
            subcategory=self.make_subcategory(**subcategory_data),
            product_name=product_name,
            code=code,
            description=description,
            valor=valor,
            discount=discount,
            price=price,
            is_new_colection=is_new_colection,
            status=status,
        )
