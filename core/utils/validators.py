from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_nik(value):
    if not value.isdigit():
        raise ValidationError(_("NIK wajib menggunakan angka."))
    if len(value) < 10 or len(value) > 16:
        raise ValidationError(
            _("Panjang NIK minimal 10 karakter dan maksimal 16 karakter.")
        )
