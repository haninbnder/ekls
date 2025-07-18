from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .forms import UserRegisterForm, UserLoginForm


# 🔐 تسجيل مستخدم جديد
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # دعم قائمة المعادن من checkboxes المتعددة
            metals_selected = request.POST.getlist("metals")
            if metals_selected:
                user.metals = ', '.join(metals_selected)

            user.save()

            print(f"✅ مستخدم جديد: {user.email} - {user.phone_number}")
            messages.success(request, "✅ تم إنشاء الحساب بنجاح. يمكنك تسجيل الدخول الآن.")
            return redirect(reverse('accounts:login'))
        else:
            print("❌ أخطاء التسجيل:", form.errors)
            messages.error(request, "❌ يوجد أخطاء في البيانات. تأكد من تعبئة الحقول بشكل صحيح.")
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# 🔐 تسجيل الدخول باستخدام البريد أو الجوال
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "✅ تم تسجيل الدخول بنجاح.")
            return redirect(reverse('core:about'))  # ← عدل المسار حسب صفحتك المطلوبة
        else:
            messages.error(request, "❌ البريد الإلكتروني أو رقم الجوال أو كلمة المرور غير صحيحة.")
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# 🔓 تسجيل الخروج
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "✅ تم تسجيل الدخول بنجاح.")
                return redirect(reverse('core:about'))  # عدّل المسار حسب الحاجة
            else:
                messages.error(request, "❌ البريد الإلكتروني أو كلمة المرور غير صحيحة.")
        else:
            messages.error(request, "❌ يرجى التأكد من صحة البيانات.")
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})
