import os
import django

# إعداد بيئة Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraplink.settings')
django.setup()

from django.contrib.auth import get_user_model

# استدعاء موديل المستخدم
User = get_user_model()

# بيانات المستخدم التلقائي
username = 'admin_ar'
email = 'admin@example.com'
password = 'admin123'
phone_number = '0500000001'  # ← رقم فريد يبدأ بـ 05 ويتكون من 10 خانات

# التحقق من وجود المستخدم مسبقًا
if not User.objects.filter(username=username).exists():
    if not User.objects.filter(phone_number=phone_number).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number
        )
        print(f'✅ تم إنشاء المستخدم: {username}')
    else:
        print(f'⚠️ رقم الجوال {phone_number} مستخدم مسبقًا.')
else:
    print(f'ℹ️ المستخدم "{username}" موجود مسبقاً.')
