from django import forms
from django.utils.safestring import mark_safe


class BaseFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_widget_styles()

    def apply_widget_styles(self):
        for field_name, field in self.fields.items():
            widget = field.widget
            if isinstance(
                widget,
                (
                    forms.TextInput,
                    forms.EmailInput,
                    forms.URLInput,
                    forms.Select,
                    forms.Textarea,
                    forms.DateInput,
                    forms.DateTimeInput,
                    forms.PasswordInput,
                    forms.NumberInput,
                ),
            ):
                widget.attrs["class"] = " ".join(
                    filter(None, [widget.attrs.get("class"), "input-control"])
                )
                if not widget.attrs.get("placeholder"):
                    widget.attrs["placeholder"] = (
                        field.label or field_name.replace("_", " ").title()
                    )


class ToggleSwitchWidget(forms.CheckboxInput):
    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs["class"] = "switch-input"
        checkbox_html = super().render(name, value, attrs, renderer)
        return mark_safe(
            f'<label class="switch">{checkbox_html}<span class="slider"></span></label>'
        )
