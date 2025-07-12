from django.urls import path
from .views import (
    product_list,
    add_product,
    unavailable_products,
    make_product_available,
    hide_product
)

app_name = 'listings'

urlpatterns = [
    # 👤 المستخدم العادي
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),

    # 🛠️ لوحة المشرف
    path('admin/unavailable/', unavailable_products, name='unavailable_products'),
    path('admin/make-available/<int:pk>/', make_product_available, name='make_product_available'),
    path('admin/hide/<int:pk>/', hide_product, name='hide_product'),
]
