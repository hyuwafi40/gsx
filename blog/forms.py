from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "content"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input-control", "placeholder": "Nama Anda"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "input-control", "placeholder": "Email Anda"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "input-control",
                    "placeholder": "Tulis komentar...",
                    "rows": 4,
                }
            ),
        }
