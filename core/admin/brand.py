from django.contrib import admin
from solo.admin import SingletonModelAdmin
from core.models import Brand


@admin.register(Brand)
class BrandAdmin(SingletonModelAdmin):
    fieldsets = (
        (None, {"fields": ("name", "description", "logo")}),
        (
            "Social Media",
            {
                "fields": ("facebook", "tiktok", "instagram", "youtube"),
                "classes": ("collapse",),
            },
        ),
    )
