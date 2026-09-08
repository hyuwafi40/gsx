from django import forms
from django.contrib.auth.models import User
from core.forms.base import BaseFormMixin
from core.utils.constants import ACCOUNT_ROLE_CHOICES_LIMITED


class AccountCreateForm(BaseFormMixin, forms.ModelForm):
    role = forms.ChoiceField(choices=ACCOUNT_ROLE_CHOICES_LIMITED)
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input-control", "placeholder": "Password"}
        ),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input-control", "placeholder": "Konfirmasi Password"}
        ),
        label="Konfirmasi Password",
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "role"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Password tidak sama.")
        return cleaned_data


class AccountUpdateForm(BaseFormMixin, forms.ModelForm):
    role = forms.ChoiceField(choices=ACCOUNT_ROLE_CHOICES_LIMITED)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-control",
                "placeholder": "Password Baru (kosongkan jika tidak diubah)",
            }
        ),
        required=False,
        label="Password Baru",
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "role"]
