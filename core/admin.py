from django.db import models
from django.utils.translation import gettext_lazy as _

class Ad(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("عنوان الإعلان")
    )
    description = models.TextField(
        verbose_name=_("الوصف")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("السعر")
    )
    image = models.ImageField(
        upload_to='ads/',
        blank=True,
        null=True,
        verbose_name=_("الصورة")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإنشاء")
    )

    class Meta:
        verbose_name = _("إعلان")
        verbose_name_plural = _("الإعلانات")
        ordering = ['-created_at']

    def __str__(self):
        return self.title
