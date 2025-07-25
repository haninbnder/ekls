from django.urls import path
from .views import home_view, contact_view, services_view, sales_view

# اسم التطبيق لتسهيل الاستدعاء في reverse() أو {% url 'core:services' %}
app_name = 'core'

urlpatterns = [
    # 🏠 الصفحة الرئيسية
    path('', home_view, name='home'),

    # 📞 صفحة تواصل معنا (عربي + إنجليزي)
    path('تواصل/', contact_view, name='contact'),
    path('contact/', contact_view),

    # 🛠️ صفحة الخدمات (عربي + إنجليزي) - تم ربطها بـ about.html
    path('الخدمات/', services_view, name='services'),
    path('services/', services_view),

    # 💰 صفحة المبيعات (عربي + إنجليزي)
    path('المبيعات/', sales_view, name='sales'),
    path('sales/', sales_view),
]
