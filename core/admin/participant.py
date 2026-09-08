from django.contrib import admin
from core.models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "stage_name",
        "name",
        "email",
        "nik",
        "gender",
        "status",
        "created_at",
    )
    list_filter = ("gender", "status", "region")
    search_fields = ("name", "stage_name", "email", "nik", "whatsapp")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Personal",
            {
                "fields": (
                    "name",
                    "stage_name",
                    "email",
                    "nik",
                    "birthdate",
                    "gender",
                    "whatsapp",
                )
            },
        ),
        (
            "Photos & Social Media",
            {
                "fields": (
                    "photo_close",
                    "photo_selfie",
                    "instagram",
                    "tiktok",
                    "facebook",
                )
            },
        ),
        ("Additional", {"fields": ("region", "invoice", "status")}),
    )
