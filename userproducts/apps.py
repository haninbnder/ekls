from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UserproductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userproducts'
    verbose_name = _("المنتجات")
