from django.urls import path
from .views import (
    register_view,
    login_view,
    # list_users_view,  # ← مؤقتًا نحذفه لأنه يسبب ImportError
    # logout_view,  # ← لاحقًا عند التفعيل
    # password_reset_view,  # ← لاحقًا لو فعلتِ استرجاع كلمة المرور
)

app_name = "accounts"  # لتفعيل namespacing عند استخدام {% url 'accounts:login' %} أو reverse()

urlpatterns = [
    # 📝 تسجيل مستخدم جديد
    path("register/", register_view, name="register"),

    # 🔐 تسجيل الدخول
    path("login/", login_view, name="login"),

    # 🐛 API مؤقت لعرض المستخدمين (محذوف مؤقتًا لتفادي الخطأ)
    # path("debug/users/", list_users_view, name="list_users"),

    # 📨 استرجاع كلمة المرور (تُفعل لاحقًا)
    # path("password-reset/", password_reset_view, name="password_reset"),
]
