from django.urls import path
from .views import user_products  # ✅ فقط استيراد عرض واحد

app_name = 'userproducts'

urlpatterns = [
    path('', user_products, name='user_products'),  # ⬅️ هذا يعرض الصفحة + يحتوي على النموذج
]
