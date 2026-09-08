from django import forms
from core.models import Participant
from core.forms.base import BaseFormMixin


class ParticipantForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            "name",
            "stage_name",
            "email",
            "nik",
            "birthdate",
            "gender",
            "whatsapp",
            "photo_close",
            "photo_selfie",
            "instagram",
            "tiktok",
            "facebook",
            "region",
            "invoice",
            "status",
        ]
        widgets = {
            "birthdate": forms.DateInput(attrs={"type": "date"}),
        }
