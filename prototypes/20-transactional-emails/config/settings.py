import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-k^h@n_zuu_y)8evs^fat$mr*#%m&u5=qwo)7(t=dvbw(0mrty&"

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "public",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1", "localhost"]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

ONBOARDING_INBOX = os.environ.get("ONBOARDING_INBOX", "hei@datakollektivet.no")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "noreply@datakollektivet.no")

DEFAULT_MAILER = os.environ.get("EMAIL_MAILER", "default")

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    },
    "scaleway": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            "host": "smtp.tem.scaleway.com",
            "port": 587,
            "use_tls": True,
            "username": os.environ.get("SCW_TEM_PROJECT_ID", ""),
            "password": os.environ.get("SCW_TEM_SECRET_KEY", ""),
        },
    },
}

# Shown on the member thank-you page and in the internal notification template.
MEMBER_PAYMENT = {
    "amount": "500 NOK",
    "account_number": "1234 56 78903",
    "reference_hint": "Use the email address you submitted as the payment reference.",
}

# Suggested-reply boilerplate in notification emails (welcomer copy/edits manually).
MATRIX_CONTACT_URL = os.environ.get("MATRIX_CONTACT_URL", "https://matrix.to/#/#datakollektivet:matrix.org")
