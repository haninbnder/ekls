from django.contrib import admin
from django.db import models
from . import models as app_models

# تسجيل جميع الموديلات القابلة للتسجيل في لوحة التحكم
for attr_name in dir(app_models):
    model = getattr(app_models, attr_name)
    if (
        isinstance(model, type) and
        issubclass(model, models.Model) and
        not model._meta.abstract
    ):
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
