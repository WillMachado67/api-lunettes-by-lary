# Generated by Django 4.2.3 on 2023-08-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_admin', '0004_alter_banner_image_banner_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_banner_mobile',
            field=models.ImageField(null=True, upload_to='cover/banner/mobile', verbose_name='Image Banner Mobile'),
        ),
    ]