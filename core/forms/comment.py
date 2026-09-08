from django import forms
from blog.models import Comment
from blog.constants import COMMENT_STATUS_CHOICES


class CommentStatusForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["status"]
        widgets = {
            "status": forms.Select(
                choices=COMMENT_STATUS_CHOICES,
                attrs={"class": "input-control"},
            ),
        }
