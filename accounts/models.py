from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    # حذف اسم المستخدم إذا ما تحتاجينه
    username = None

    # رقم الجوال - يجب أن يكون فريدًا ويتكون من 10 أرقام
    phone_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="رقم الجوال"
    )

    # هل المستخدم هو مشتري؟ (تاجر معادن)
    is_collector = models.BooleanField(
        default=False,
        verbose_name="هل أنت مشتري؟"
    )

    # البريد الإلكتروني كمفتاح تسجيل دخول
    email = models.EmailField(
        unique=True,
        verbose_name="البريد الإلكتروني"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']  # الحقول المطلوبة عند إنشاء مستخدم superuser

    def __str__(self):
        return self.email
