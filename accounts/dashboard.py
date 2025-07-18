from django.contrib.admin import AdminSite
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from datetime import timedelta

User = get_user_model()

def get_recent_users(limit=5):
    week_ago = now() - timedelta(days=7)
    recent_users = User.objects.filter(date_joined__gte=week_ago).order_by('-date_joined')[:limit]
    rows = ""

    for user in recent_users:
        link = reverse("admin:accounts_customuser_change", args=[user.pk])
        rows += f"<li><a href='{link}'>{user.username}</a> - {user.date_joined.strftime('%Y-%m-%d %H:%M')}</li>"

    if not rows:
        rows = "<li>لا يوجد مستخدمون جدد</li>"

    return format_html(f"""
        <div class='card'>
            <div class='card-header'><strong>🟢 المستخدمون الجدد (آخر 7 أيام)</strong></div>
            <ul class='card-body'>{rows}</ul>
        </div>
    """)
