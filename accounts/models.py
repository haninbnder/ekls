from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # هل المستخدم هو مشتري؟ (تاجر معادن)
    is_collector = models.BooleanField(
        default=False,
        verbose_name='هل أنت مشتري؟'
    )

    # رقم الجوال - يجب أن يكون فريدًا ويتكون من 10 أرقام
    phone_number = models.CharField(
        max_length=10,
        unique=True
    )
