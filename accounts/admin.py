from django.contrib import admin
from . import models
from django.db import models as django_models

# ✅ تسجيل جميع الموديلات داخل التطبيق ما عدا المجردة
for model_name in dir(models):
    model = getattr(models, model_name)

    if (
        isinstance(model, type)
        and issubclass(model, django_models.Model)
        and not model._meta.abstract  # استبعاد الموديلات المجردة
        and hasattr(model._meta, 'app_label')
    ):
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass  # تجاهل الموديلات المسجلة سابقًا

# ✅ إضافة ويدجت المستخدمين الجدد في لوحة المشرف (Dashboard)
from accounts.dashboard import get_recent_users

admin.site.index_template = "admin/custom_index.html"
admin.site.get_recent_users = get_recent_users
