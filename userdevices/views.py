from django.shortcuts import render, get_object_or_404
from listings.models import Product

# ✅ عرض المنتجات الخاصة بالمستخدم (مثال عام - يمكن تخصيصه لاحقًا حسب المستخدم الحالي)
def user_products(request):
    # لاحقًا يمكن فلترة المنتجات حسب المستخدم إن كان هناك علاقة
    products = Product.objects.all()
    return render(request, 'userproducts/user_products.html', {'products': products})

# ✅ عرض صفحة إضافة منتج (نموذج مبسط - بدون نموذج إدخال حالياً)
def add_product(request):
    return render(request, 'userproducts/add_product.html')
