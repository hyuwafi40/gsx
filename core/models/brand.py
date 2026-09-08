from django.db import models
from solo.models import SingletonModel
from core.models.base import TimeStampedModel
from core.utils.constants import URL_MAX_LENGTH


class Brand(SingletonModel, TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logo = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    facebook = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    tiktok = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    instagram = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    youtube = models.URLField(max_length=URL_MAX_LENGTH, blank=True)

    def __str__(self):
        return self.name
