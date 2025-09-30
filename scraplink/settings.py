from pathlib import Path
import os
from dotenv import load_dotenv

# --------------------------------------------------
# تحميل متغيرات البيئة من ملف .env (محليًا فقط)
# --------------------------------------------------
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# متغيرات البيئة والأمان
# --------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")
DEBUG = os.getenv("DEBUG", "False") == "True"

# ALLOWED_HOSTS من البيئة، وإن لم تُحدَّد نضيف localhost و Render
_env_hosts = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "").split(",") if h.strip()]
if _env_hosts:
    ALLOWED_HOSTS = _env_hosts
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".onrender.com"]

# CSRF_TRUSTED_ORIGINS من البيئة، مع قيمة افتراضية تدعم Render
_env_csrf = [o.strip() for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()]
if _env_csrf:
    CSRF_TRUSTED_ORIGINS = _env_csrf
else:
    # لاحظ أن Django يتطلب https:// في القيم
    CSRF_TRUSTED_ORIGINS = [
        "https://*.onrender.com",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]

# --------------------------------------------------
# التطبيقات المثبتة
# --------------------------------------------------
INSTALLED_APPS = [
    "corsheaders",  # لدعم CORS
    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # تطبيقات المشروع
    "accounts",
    "appointments",
    "listings",
    "core",
    "orders",
    "userproducts",
    "useritems",
    "user_devices",
    # أضِفِ "rest_framework" إن كنتِ تستخدمين DRF في الـ views/serializers
    # "rest_framework",
]

# --------------------------------------------------
# إعدادات Jazzmin (كما هي)
# --------------------------------------------------
JAZZMIN_SETTINGS = {
    "site_title": "لوحة إدارة سكربلينك",
    "site_header": "إدارة سكربلينك",
    "site_brand": "SKRAP LINK",
    "welcome_sign": "مرحباً بك في لوحة التحكم",
    "site_logo": "/static/images/logo.png",
    "site_icon": "/static/images/logo.png",
    "login_logo": "/static/images/logo.png",
    "login_logo_dark": "/static/images/logo.png",
    "site_logo_classes": "img-circle elevation-2",
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "navigation_expanded": False,
    "order_with_respect_to": [
        "core", "accounts", "listings", "appointments",
        "userproducts", "orders", "useritems", "user_devices",
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
    "custom_css": "/static/jazzmin/admin_custom.css",
    "custom_js": None,
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "language_chooser": False,
}

# --------------------------------------------------
# Middleware
# --------------------------------------------------
# الترتيب الموصى به لـ WhiteNoise و CORS:
# Security -> WhiteNoise -> (Cors) -> Session -> Locale -> Common -> ...
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "listings.middleware.ForceArabicMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# CORS (يمكن تقييدها لاحقًا عبر البيئة)
# --------------------------------------------------
# مؤقتًا يسمح للجميع إذا لم تُحدَّد قائمة عبر البيئة
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", "True") == "True"

# بديل أكثر أمانًا: حدّدي origins عبر CORS_ALLOWED_ORIGINS
_env_cors = [o.strip() for o in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if o.strip()]
if _env_cors:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = _env_cors

# إن احتجتِ الكوكيز عبر CORS
CORS_ALLOW_CREDENTIALS = os.getenv("CORS_ALLOW_CREDENTIALS", "False") == "True"

# --------------------------------------------------
# القوالب و WSGI
# --------------------------------------------------
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

# --------------------------------------------------
# قاعدة البيانات
# --------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", str(BASE_DIR / "db.sqlite3")),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}

# --------------------------------------------------
# تحقق كلمة المرور
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------
# اللغة والتوقيت
# --------------------------------------------------
LANGUAGE_CODE = "ar"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [("ar", "العربية")]
LOCALE_PATHS = [BASE_DIR / "locale"]

# --------------------------------------------------
# static / media و WhiteNoise
# --------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # إن لم يوجد مجلد static محليًا يمكنك إزالة هذا
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# تخزين مضغوط مع manifest (مناسب للإنتاج مع collectstatic)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------
# مصادقة ومسارات
# --------------------------------------------------
AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

AUTHENTICATION_BACKENDS = [
    "accounts.backends.EmailOrPhoneBackend",
    "django.contrib.auth.backends.ModelBackend",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------
# البريد (تجريبي)
# --------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# --------------------------------------------------
# أمان إضافي للإنتاج
# --------------------------------------------------
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "False") == "True"
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "False") == "True"
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", "False") == "True"
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", 0))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.getenv("SECURE_HSTS_INCLUDE_SUBDOMAINS", "False") == "True"
SECURE_HSTS_PRELOAD = os.getenv("SECURE_HSTS_PRELOAD", "False") == "True"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
