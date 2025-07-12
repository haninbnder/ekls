from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse

# ✅ عرض صفحة إضافة منتج
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings:product_list')
    else:
        form = ProductForm()
    return render(request, 'listings/add_product.html', {'form': form})

# ✅ عرض كل المنتجات المتاحة فقط
def product_list(request):
    products = Product.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'listings/product_list.html', {'products': products})

# ✅ للمشرف: عرض المنتجات غير المتاحة
@staff_member_required
def unavailable_products(request):
    products = Product.objects.filter(is_available=False)
    return render(request, 'listings/admin_unavailable_products.html', {'products': products})

# ✅ للمشرف: إتاحة منتج
@staff_member_required
def make_product_available(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_available = True
    product.save()
    return redirect('listings:unavailable_products')

# ✅ للمشرف: إخفاء منتج من المتجر
@staff_member_required
def hide_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_available = False
    product.save()
    return redirect('listings:unavailable_products')
