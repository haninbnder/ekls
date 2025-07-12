import sqlite3
from django.conf import settings

def check_product_columns():
    db_path = settings.DATABASES['default']['NAME']
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # جلب أسماء الأعمدة من جدول المنتجات
    cursor.execute("PRAGMA table_info(listings_product);")
    columns = cursor.fetchall()
    conn.close()

    print("🧩 الأعمدة الموجودة حاليًا في جدول Product:\n")
    for col in columns:
        print(f"- {col[1]}")

    expected_fields = [
        'id', 'owner_id', 'name', 'description', 'quantity',
        'price', 'category', 'condition', 'is_available',
        'image', 'location', 'created_at', 'updated_at'
    ]

    print("\n📋 مقارنة الأعمدة المتوقعة مع الموجودة:\n")
    for field in expected_fields:
        if field not in [col[1] for col in columns]:
            print(f"❌ مفقود: {field}")
        else:
            print(f"✅ موجود: {field}")

if __name__ == "__main__":
    import django
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scraplink.settings")
    django.setup()
    check_product_columns()
