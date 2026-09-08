from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ParticipantManager(models.Manager):
    def registered(self):
        return self.get_queryset().filter(status="registered")

    def verified(self):
        return self.get_queryset().filter(status="verified")
