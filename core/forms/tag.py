from django import forms
from blog.models import Tag
from core.forms.base import BaseFormMixin


class TagForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
