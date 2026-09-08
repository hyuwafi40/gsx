from django import forms
from core.models import Brand
from core.forms.base import BaseFormMixin


class BrandForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            "name",
            "description",
            "logo",
            "facebook",
            "tiktok",
            "instagram",
            "youtube",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
