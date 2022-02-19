from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShopwindowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopwindow'
    verbose_name = 'Вітрини'
