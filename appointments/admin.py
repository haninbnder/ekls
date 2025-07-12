from django.db import models
from django.conf import settings

class Appointment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )
    material_type = models.CharField(
        max_length=50,
        verbose_name="نوع المادة"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="الكمية (بالكيلو)"
    )
    appointment_date = models.DateField(
        verbose_name="تاريخ الموعد"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="ملاحظات إضافية"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.material_type} في {self.appointment_date}"
