from django.db import models
from django.conf import settings  # ✅ لاستخدام CustomUser
from listings.models import Product  # تأكد أن لديك تطبيق listings يحتوي على Product
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', _('قيد الانتظار')),
        ('approved', _('تم القبول')),
        ('shipped', _('تم الشحن')),
        ('delivered', _('تم التسليم')),
        ('canceled', _('تم الإلغاء')),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ✅ استخدام النموذج المخصص
        on_delete=models.CASCADE,
        verbose_name=_("المستخدم")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("المنتج")
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("الكمية")
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name=_("الحالة")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإنشاء")
    )

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب رقم {self.id} من {self.user.username}"
