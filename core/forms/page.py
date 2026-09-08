from django import forms
from blog.models import Page
from core.forms.base import BaseFormMixin


class PageForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Page
        fields = ["title", "content", "status"]
