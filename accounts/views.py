from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .forms import UserRegisterForm, UserLoginForm


# 🔐 عرض نموذج تسجيل مستخدم جديد ومعالجة بيانات التسجيل
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"✅ مستخدم جديد: {user.username} - {user.phone_number}")
            messages.success(request, "تم إنشاء الحساب بنجاح. يمكنك تسجيل الدخول الآن.")
            return redirect(reverse('accounts:login'))
        else:
            messages.error(request, "تحقق من البيانات المدخلة.")
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# 🔐 تسجيل دخول المستخدم باستخدام اسم المستخدم أو رقم الجوال
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح.")
            return redirect(reverse('core:about'))  # ← تحويل المستخدم إلى صفحة "عن المشروع"
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# 🔓 تسجيل الخروج من الحساب وإعادة التوجيه إلى صفحة تسجيل الدخول
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح.")
    return redirect(reverse('accounts:login'))


# 🐛 فيو مؤقت لعرض المستخدمين الحاليين (لتأكيد نجاح التسجيل على Render)
def list_users_view(request):
    User = get_user_model()
    users = User.objects.all().values("username", "phone_number", "date_joined")
    return JsonResponse(list(users), safe=False)
