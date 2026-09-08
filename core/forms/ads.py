from django import forms
from blog.models import Advertisement
from core.forms.base import BaseFormMixin


class AdsForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["name", "type_ads", "image", "link", "end_date", "status"]
        widgets = {
            "end_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "status": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
