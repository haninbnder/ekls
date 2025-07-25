from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# ✅ الصفحة الرئيسية
def home_view(request):
    return render(request, 'core/home.html')

# ℹ️ صفحة من نحن
def about_view(request):
    return render(request, 'core/about.html')

# 📞 صفحة تواصل معنا
def contact_view(request):
    return render(request, 'core/contact.html')

# 🛠️ صفحة الخدمات (تحوّل إلى about.html)
@login_required(login_url='accounts:login')
def services_view(request):
    # تم التوجيه إلى about.html بدلًا من services.html
    return render(request, 'core/about.html')

# 💰 صفحة المبيعات (تتطلب تسجيل دخول)
@login_required(login_url='accounts:login')
def sales_view(request):
    return render(request, 'core/sales.html')




