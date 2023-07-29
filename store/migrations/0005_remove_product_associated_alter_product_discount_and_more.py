# Generated by Django 4.2.3 on 2023-07-29 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('store', '0004_alter_product_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='associated',
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Desconto %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(limit_choices_to={'category_id': '1'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.subcategory', verbose_name='Subcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='valor',
            field=models.FloatField(verbose_name='Valor R$'),
        ),
    ]
