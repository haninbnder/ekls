from django.db import models
from django.conf import settings

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'إلكترونيات'),
        ('furniture', 'أثاث'),
        ('metal', 'معادن'),
        ('other', 'أخرى'),
    ]

    CONDITION_CHOICES = [
        ('new', 'جديد'),
        ('used', 'مستعمل'),
    ]

    # ✅ جعل الحقل اختياريًا أثناء التطوير
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='صاحب المنتج',
        null=True,       # ← يسمح بأن يكون فارغًا في قاعدة البيانات
        blank=True       # ← يسمح بتركه فارغًا في الفورم
    )

    name = models.CharField(max_length=255, verbose_name='اسم المنتج')
    description = models.TextField(blank=True, verbose_name='الوصف')
    quantity = models.PositiveIntegerField(default=1, verbose_name='الكمية')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other', verbose_name='الفئة')
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='used', verbose_name='الحالة')
    is_available = models.BooleanField(default=True, verbose_name='متاح للبيع')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='صورة المنتج')
    location = models.CharField(max_length=255, default="الرياض", verbose_name='الموقع')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخر تعديل')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']
