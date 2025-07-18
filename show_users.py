import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scraplink.settings")
django.setup()

from accounts.models import CustomUser

for user in CustomUser.objects.all():
    print(f"{user.username} - {user.email} - {user.date_joined}")
