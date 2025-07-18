from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# العروض المباشرة من التطبيقات
from accounts.views import login_view
from listings.views import add_product
from core.views import about_view, sales_view

urlpatterns = [
    # لوحة التحكم
    path("admin/", admin.site.urls),

    # روابط مباشرة للعروض
    path("login/", login_view, name="direct_login"),
    path("add-product/", add_product, name="direct_add_product"),
    path("sales/", sales_view, name="sales"),
    path("about/", about_view, name="about"),

    # روابط التطبيقات
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("listings/", include(("listings.urls", "listings"), namespace="listings")),
    path("my-products/", include(("userproducts.urls", "userproducts"), namespace="userproducts")),
    path("orders/", include(("orders.urls", "orders"), namespace="orders")),

    # الصفحة الرئيسية
    path("", include(("core.urls", "core"), namespace="core")),
]

# ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
