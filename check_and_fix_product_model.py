import os
import django
import sqlite3
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraplink.settings')
django.setup()

from listings.models import Product
from django.db import connection

def check_missing_columns():
    expected_fields = [f.column for f in Product._meta.fields]
    table_name = Product._meta.db_table

    with connection.cursor() as cursor:
        cursor.execute(f"PRAGMA table_info({table_name});")
        existing_columns = [row[1] for row in cursor.fetchall()]

    missing = [field for field in expected_fields if field not in existing_columns]
    return missing

def auto_fix_schema():
    missing = check_missing_columns()

    if not missing:
        print("✅ لا توجد أعمدة ناقصة. قاعدة البيانات متزامنة مع الموديل.")
        return

    print("⚠️ تم العثور على أعمدة ناقصة في جدول المنتجات:")
    for col in missing:
        print(f" - {col}")

    print("\n🛠️ جاري تنفيذ أوامر makemigrations و migrate تلقائيًا...")

    os.system("python manage.py makemigrations listings")
    os.system("python manage.py migrate")

    print("✅ تم إصلاح المخطط بنجاح.")

if __name__ == '__main__':
    auto_fix_schema()
