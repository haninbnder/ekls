from django.urls import path
from .views import register_view, login_view, logout_view, list_users_view

app_name = 'accounts'  # لتفعيل namespacing عند استخدام reverse أو {% url %}

urlpatterns = [
    # تسجيل مستخدم جديد
    path('register/', register_view, name='register'),

    # تسجيل الدخول
    path('login/', login_view, name='login'),

    # تسجيل الخروج
    path('logout/', logout_view, name='logout'),

    # ✅ عرض المستخدمين (فقط للتجربة والتحقق على السيرفر)
    path('debug/users/', list_users_view, name='list_users'),

    # ✔️ ملاحظة مستقبلية: استعادة كلمة المرور
    # يمكن تفعيلها لاحقًا بسهولة باستخدام auth_views
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
