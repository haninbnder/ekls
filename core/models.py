from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Location(models.Model):
    city = models.CharField(max_length=100, verbose_name=_("المدينة"))
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_("تاريخ الإضافة"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاريخ التحديث"))

    class Meta:
        verbose_name = _("موقع")
        verbose_name_plural = _("المواقع")
        ordering = ['city']  # ترتيب أبجدي حسب المدينة

    def __str__(self):
        return f"{self.city}"
