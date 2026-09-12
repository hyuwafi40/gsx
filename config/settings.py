# import os
# from pathlib import Path
# from decouple import config
# import dj_database_url

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = config(
#     "DJANGO_SECRET_KEY", default="django-insecure-temporary-key-change-me"
# )

# DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)

# ALLOWED_HOSTS = [
#     host.strip()
#     for host in config(
#         "DJANGO_ALLOWED_HOSTS", default=".vercel.app,localhost,127.0.0.1"
#     ).split(",")
# ]

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "django_ckeditor_5",
#     "django_htmx",
#     "solo",
#     "guardian",
#     "core",
#     "blog",
#     "django_cleanup",
# ]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django_htmx.middleware.HtmxMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# AUTHENTICATION_BACKENDS = [
#     "django.contrib.auth.backends.ModelBackend",
#     "guardian.backends.ObjectPermissionBackend",
# ]

# ROOT_URLCONF = "config.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [BASE_DIR / "templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#                 "core.context_processors.brand_info",
#                 "core.context_processors.global_partials",
#                 "blog.context_processors.global_blog_partials",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "config.wsgi.application"

# DATABASE_URL = config("DJANGO_DATABASE_URL", default="sqlite:///db.sqlite3")
# DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}

# AUTH_PASSWORD_VALIDATORS = [
#     {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
# ]

# LANGUAGE_CODE = "en-us"
# TIME_ZONE = config("DJANGO_TIME_ZONE", default="Asia/Jakarta")
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = "/static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGIN_URL = "login"
# LOGIN_REDIRECT_URL = "core:index"
# LOGOUT_REDIRECT_URL = "login"

# CKEDITOR_5_CONFIGS = {
#     "default": {
#         "toolbar": [
#             "undo",
#             "redo",
#             "|",
#             "heading",
#             "|",
#             "bold",
#             "italic",
#             "underline",
#             "link",
#             "|",
#             "bulletedList",
#             "numberedList",
#             "alignment",
#             "outdent",
#             "indent",
#             "|",
#             "blockQuote",
#             "insertTable",
#             "imageUpload",
#             "imageInsert",
#             "mediaEmbed",
#             "|",
#             "removeFormat",
#         ],
#     },
# }

# APP_SCRIPT_TOKEN = config("APP_SCRIPT_TOKEN")


import os
from pathlib import Path
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("DJANGO_SECRET_KEY")

DEBUG = config("DJANGO_DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    host.strip()
    for host in config(
        "DJANGO_ALLOWED_HOSTS",
        default="localhost,127.0.0.1",
    ).split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in config(
        "CSRF_TRUSTED_ORIGINS",
        default="",
    ).split(",")
    if origin.strip()
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_ckeditor_5",
    "django_htmx",
    "solo",
    "guardian",
    "core",
    "blog",
    "django_cleanup",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
]

ROOT_URLCONF = "config.urls"

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
                "core.context_processors.brand_info",
                "core.context_processors.global_partials",
                "blog.context_processors.global_blog_partials",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASE_URL = config("DJANGO_DATABASE_URL", default="sqlite:///db.sqlite3")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = config("DJANGO_TIME_ZONE", default="Asia/Jakarta")
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "core:index"
LOGOUT_REDIRECT_URL = "login"

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload",
            "imageInsert",
        ],
    },
}

APP_SCRIPT_TOKEN = config("APP_SCRIPT_TOKEN")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")