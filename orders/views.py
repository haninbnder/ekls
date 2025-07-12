from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def order_list(request):
    """
    عرض جميع الطلبات الخاصة بالمستخدم الحالي.
    """
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_create(request):
    """
    إنشاء طلب جديد.
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

@login_required
def order_detail(request, pk):
    """
    عرض تفاصيل طلب محدد للمستخدم الحالي.
    """
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
