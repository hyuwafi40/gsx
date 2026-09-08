from django import forms
from blog.models import Album, Photos
from core.forms.base import BaseFormMixin


class AlbumForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name", "thumbnail", "description", "status"]


class PhotoForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Photos
        fields = ["name", "image", "caption"]
