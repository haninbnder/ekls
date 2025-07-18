from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# العروض المباشرة
from accounts.views import login_view
from listings.views import add_product
from core.views import about_view, sales_view  # ✅ about + sales

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # روابط مباشرة
    path('login/', login_view, name='direct_login'),
    path('add-product/', add_product, name='direct_add_product'),
    path('sales/', sales_view, name='sales'),

    # about كعرض مباشر
    path('about/', about_view, name='about'),

    # روابط التطبيقات
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('listings/', include('listings.urls')),
    path('my-products/', include('userproducts.urls', namespace='userproducts')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('', include('core.urls')),  # ← يستدعي core.urls ومنها الصفحة الرئيسية
]

# إعدادات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
