import os
import django

# إعداد البيئة لتحميل إعدادات Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scraplink.settings")
django.setup()

from accounts.models import CustomUser

def list_users():
    users = CustomUser.objects.all()
    if not users:
        print("لا يوجد مستخدمون حالياً.")
        return

    print("📋 قائمة المستخدمين:\n")
    for user in users:
        print(f"👤 {user.username} | 📧 {user.email or 'بدون بريد'} | 🗓️ {user.date_joined}")

if __name__ == "__main__":
    list_users()
