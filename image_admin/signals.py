import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from .models import Banner


@receiver(pre_delete, sender=Banner)
def delete_banner_images(sender, instance, **kwargs):
    if instance.image_banner_desktop:
        if os.path.isfile(instance.image_banner_desktop.path):
            os.remove(instance.image_banner_desktop.path)

    if instance.image_banner_mobile:
        if os.path.isfile(instance.image_banner_mobile.path):
            os.remove(instance.image_banner_mobile.path)


@receiver(pre_save, sender=Banner)
def delete_old_banner_images(sender, instance, **kwargs):
    if instance.pk:
        original = Banner.objects.get(pk=instance.pk)
        if original.image_banner_desktop != instance.image_banner_desktop:
            if original.image_banner_desktop:
                if os.path.isfile(original.image_banner_desktop.path):
                    os.remove(original.image_banner_desktop.path)

        if original.image_banner_mobile != instance.image_banner_mobile:
            if original.image_banner_mobile:
                if os.path.isfile(original.image_banner_mobile.path):
                    os.remove(original.image_banner_mobile.path)
