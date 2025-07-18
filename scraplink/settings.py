from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()  # تحميل متغيرات البيئة من ملف .env

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# متغيرات البيئة
# -------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")
DEBUG = os.getenv("DEBUG", "False") == "True"

# ✅ إصلاح ALLOWED_HOSTS ليكون قائمة
ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if host.strip()]

# -------------------------------
# التطبيقات المثبتة
# -------------------------------
INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "appointments",
    "listings",
    "core",
    "orders",
    "userproducts",
    "useritems",
    "user_devices",
]

# -------------------------------
# إعدادات Jazzmin
# -------------------------------
JAZZMIN_SETTINGS = {
    "site_title": "لوحة إدارة سكربلينك",
    "site_header": "إدارة سكربلينك",
    "site_brand": "SKRAP LINK",
    "welcome_sign": "مرحباً بك في لوحة التحكم",
    "copyright": "جميع الحقوق محفوظة © 2025",
    "site_logo": "images/logo.png",
    "site_icon": "images/logo.png",
    "login_logo": "images/logo.png",
    "login_logo_dark": "images/logo.png",
    "site_logo_classes": "img-circle elevation-2",
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "navigation_expanded": False,
    "order_with_respect_to": [
        "core",
        "accounts",
        "listings",
        "appointments",
        "userproducts",
        "orders",
        "useritems",
        "user_devices",
    ],
    "icons": {
        "core.Location": "fas fa-map-marker-alt",
        "accounts.CustomUser": "fas fa-user-shield",
        "listings.Product": "fas fa-box",
        "appointments.Appointment": "fas fa-calendar-check",
        "userproducts.MyProduct": "fas fa-warehouse",
        "orders.Order": "fas fa-clipboard-list",
        "auth.User": "fas fa-users-cog",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "hide_apps": [],
    "hide_models": [],
    "changeform_format": "horizontal_tabs",
    "custom_css": "jazzmin/admin_custom.css",
    "custom_js": None,
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "language_chooser": False,
}

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "listings.middleware.ForceArabicMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "scraplink.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "scraplink.wsgi.application"

# -------------------------------
# قاعدة البيانات
# -------------------------------
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}

# -------------------------------
# التحقق من كلمات المرور
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "ar"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [("ar", "العربية")]
LOCALE_PATHS = [BASE_DIR / "locale"]

# -------------------------------
# ملفات static/media
# -------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------------
# مصادقة
# -------------------------------
AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_REDIRECT_URL = "/services/"
LOGOUT_REDIRECT_URL = "/login/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -------------------------------
# إعدادات أمان HTTPS
# -------------------------------
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "False") == "True"
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "False") == "True"
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "False") == "True"
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", 0))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.getenv("SECURE_HSTS_INCLUDE_SUBDOMAINS", "False") == "True"
SECURE_HSTS_PRELOAD = os.getenv("SECURE_HSTS_PRELOAD", "False") == "True"
SECURE_PROXY_SSL_HEADER = None
