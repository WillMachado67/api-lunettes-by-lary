# Generated by Django 4.2.3 on 2023-07-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_discount_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=25, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='valor',
            field=models.FloatField(verbose_name='Valor R$'),
        ),
    ]