import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from .models import Banner, ImageProduct, PersonalizedService


def delete_image(instance, field_name):
    if field_name:
        try:
            file_path = getattr(instance, field_name).path
            os.remove(file_path)
        except FileNotFoundError:
            pass


def create_image_delete_receiver(model):
    @receiver(pre_delete, sender=model)
    def image_delete(sender, instance, **kwargs):
        delete_image(instance, 'image_desktop')
        delete_image(instance, 'image_mobile')


def create_image_update_receiver(model):
    @receiver(pre_save, sender=model)
    def image_update(sender, instance, **kwargs):
        if instance.pk:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image_desktop != instance.image_desktop:
                delete_image(old_instance, 'image_desktop')
            if old_instance.image_mobile != instance.image_mobile:
                delete_image(old_instance, 'image_mobile')


create_image_delete_receiver(Banner)
create_image_update_receiver(Banner)

create_image_delete_receiver(PersonalizedService)
create_image_update_receiver(PersonalizedService)


@receiver(pre_delete, sender=ImageProduct)
def image_delete(sender, instance, **kwargs):
    delete_image(instance, 'image_1')
    delete_image(instance, 'image_2')
    delete_image(instance, 'image_3')


@receiver(pre_save, sender=ImageProduct)
def image_update(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.image_1 != instance.image_1:
            delete_image(old_instance, 'image_1')
        if old_instance.image_2 != instance.image_2:
            delete_image(old_instance, 'image_2')
        if old_instance.image_3 != instance.image_3:
            delete_image(old_instance, 'image_3')
