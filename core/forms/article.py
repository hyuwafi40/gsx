from django import forms
from blog.models import Article, Tag
from core.forms.base import BaseFormMixin, ToggleSwitchWidget


class ArticleForm(BaseFormMixin, forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "tag-checkbox-list"}),
        required=False,
    )
    is_important = forms.BooleanField(widget=ToggleSwitchWidget(), required=False)

    class Meta:
        model = Article
        fields = [
            "title",
            "thumbnail",
            "category",
            "tag",
            "content",
            "status",
            "is_important",
        ]
