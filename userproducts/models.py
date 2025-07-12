from django.db import models
from django.conf import settings

class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    type = models.CharField(max_length=100, verbose_name="نوع المنتج")  # ✅ جديد
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="الوزن (كجم)")  # ✅ جديد
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر (ريال)")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="صورة المنتج")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
