from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    """
    عرض الصفحة الرئيسية.
    """
    return render(request, 'core/home.html')

def about_view(request):
    """
    عرض صفحة من نحن.
    """
    return render(request, 'core/about.html')

def contact_view(request):
    """
    عرض صفحة تواصل معنا.
    """
    return render(request, 'core/contact.html')

@login_required(login_url='accounts:login')
def services_view(request):
    """
    عرض صفحة الخدمات (تتطلب تسجيل دخول).
    """
    return render(request, 'core/services.html')

@login_required(login_url='accounts:login')
def sales_view(request):
    """
    عرض صفحة المبيعات (تتطلب تسجيل دخول).
    """
    return render(request, 'core/sales.html')
