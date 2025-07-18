from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    list_users_view,
    # password_reset_view,  # ← لاحقًا لو فعلتِ استرجاع كلمة المرور
)

app_name = "accounts"  # لتفعيل namespacing عند استخدام {% url 'accounts:login' %} أو reverse()

urlpatterns = [
    # 📝 تسجيل مستخدم جديد
    path("register/", register_view, name="register"),

    # 🔐 تسجيل الدخول
    path("login/", login_view, name="login"),

    # 🔓 تسجيل الخروج
    path("logout/", logout_view, name="logout"),

    # 🐛 API مؤقت لعرض المستخدمين (لتجربة على Render مثلاً)
    path("debug/users/", list_users_view, name="list_users"),

    # 📨 استرجاع كلمة المرور (تُفعل لاحقًا)
    # path("password-reset/", password_reset_view, name="password_reset"),
]
