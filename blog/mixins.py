from django.conf import settings
from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        related_name="%(class)s_created_by",
    )

    def created_by_full_name(self):
        if self.created_by:
            return self.created_by.get_full_name() or self.created_by.username
        return ""

    class Meta:
        abstract = True
