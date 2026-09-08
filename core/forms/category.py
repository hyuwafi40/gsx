from django import forms
from blog.models import Category
from core.forms.base import BaseFormMixin


class CategoryForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
