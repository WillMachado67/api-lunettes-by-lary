# Generated by Django 4.2.3 on 2023-08-15 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_admin', '0002_alter_banner_image_banner_desktop'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image_banner_mobile',
            field=models.ImageField(null=True, upload_to='cover/banner/mobile', verbose_name='Image Banner Mobile'),
        ),
    ]
