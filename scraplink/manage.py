#!/usr/bin/env python
"""أداة إدارة مشروع Django لـ Scraplink."""
import os
import sys
from datetime import datetime
import shutil

def backup_requirements():
    """إنشاء نسخة احتياطية تلقائيًا من ملف requirements.txt"""
    src = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(src):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        dst = os.path.join(os.path.dirname(__file__), f'requirements_backup_{timestamp}.txt')
        shutil.copy(src, dst)
        print(f"✅ تم إنشاء نسخة احتياطية من requirements.txt → {dst}")
    else:
        print("⚠️ لم يتم العثور على ملف requirements.txt")

def main():
    """نقطة الدخول الرئيسية."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraplink.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "تعذّر استيراد Django. تأكد من تثبيته وتفعيل البيئة الافتراضية."
        ) from exc

    # تفعيل النسخ التلقائي عند تشغيل runserver فقط
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        backup_requirements()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
