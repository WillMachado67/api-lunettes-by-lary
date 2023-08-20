# Generated by Django 4.2.3 on 2023-08-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Image Banner', max_length=25)),
                ('image_banner_desktop', models.ImageField(upload_to='cover/banner/desktop', verbose_name='Image Banner Desktop')),
                ('image_banner_mobile', models.ImageField(null=True, upload_to='cover/banner/mobile', verbose_name='Image Banner Mobile')),
            ],
        ),
    ]
