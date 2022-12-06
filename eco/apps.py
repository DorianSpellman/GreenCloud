from django.apps import AppConfig


class EcoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eco'
    verbose_name = 'Green Cloud' # "многословное имя", отображаемое в админ панеле
