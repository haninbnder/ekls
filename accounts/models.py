from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# ✅ مدير مخصص لإنشاء المستخدمين والمستخدمين الإداريين
class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("يجب إدخال البريد الإلكتروني")
        if not phone_number:
            raise ValueError("يجب إدخال رقم الجوال")

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("المستخدم الإداري يجب أن يكون is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("المستخدم الإداري يجب أن يكون is_superuser=True")

        return self.create_user(email, phone_number, password, **extra_fields)


# ✅ موديل المستخدم المخصص بالبريد فقط
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    phone_number = models.CharField(max_length=10, unique=True, verbose_name="رقم الجوال")
    full_name = models.CharField(max_length=150, verbose_name="الاسم الكامل")
    is_collector = models.BooleanField(default=False, verbose_name="هل أنت مشتري؟")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
