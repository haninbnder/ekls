from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from listings.models import Product
from .forms import ProductForm

@login_required
def user_products(request):
    """عرض وإضافة منتجات المستخدم الحالي"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user  # ✅ التعديل الصحيح
            product.save()
            return redirect('userproducts:user_products')
    else:
        form = ProductForm()

    products = Product.objects.filter(owner=request.user)  # ✅ التعديل الصحيح

    return render(request, 'userproducts/user_products.html', {
        'form': form,
        'products': products
    })
