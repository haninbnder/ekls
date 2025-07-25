from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# ✅ الصفحة الرئيسية
def home_view(request):
    """
    عرض الصفحة الرئيسية.
    """
    return render(request, 'core/home.html')

# ℹ️ صفحة من نحن
def about_view(request):
    """
    عرض صفحة من نحن.
    """
    return render(request, 'core/about.html')

# 📞 صفحة تواصل معنا
def contact_view(request):
    """
    عرض صفحة تواصل معنا.
    """
    return render(request, 'core/contact.html')

# 🛠️ صفحة الخدمات (تتطلب تسجيل دخول)
@login_required(login_url='accounts:login')
def services_view(request):
    """
    عرض صفحة الخدمات (تتطلب تسجيل دخول).
    """
    return render(request, 'core/services.html')

# 💰 صفحة المبيعات (تتطلب تسجيل دخول)
@login_required(login_url='accounts:login')
def sales_view(request):
    """
    عرض صفحة المبيعات (تتطلب تسجيل دخول).
    """
    return render(request, 'core/sales.html')
