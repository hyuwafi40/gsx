from django import forms
from blog.models import Carousel
from core.forms.base import BaseFormMixin


class CarouselForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ["name", "image", "ordering"]
