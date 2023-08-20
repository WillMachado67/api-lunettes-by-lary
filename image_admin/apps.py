from django.apps import AppConfig


class ImageAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_admin'

    def ready(self, *args, **kwargs):
        import image_admin.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
