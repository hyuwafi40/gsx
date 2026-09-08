# from django.db import models
# from core.models.base import TimeStampedModel
# from core.utils.constants import GENDER_CHOICES, STATUS_CHOICES, URL_MAX_LENGTH
# from core.utils.validators import validate_nik


# class Participant(TimeStampedModel):
#     name = models.CharField(max_length=100)
#     stage_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     nik = models.CharField(max_length=16, unique=True, validators=[validate_nik])
#     birthdate = models.DateField()
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     whatsapp = models.CharField(max_length=20)
#     photo_close = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
#     photo_selfie = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
#     instagram = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
#     tiktok = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
#     facebook = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
#     region = models.CharField(max_length=100)
#     invoice = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
#     status = models.CharField(
#         max_length=20, choices=STATUS_CHOICES, default="registered"
#     )

#     def __str__(self):
#         return f"{self.stage_name} - {self.name}"
from django.db import models
from core.models.base import TimeStampedModel
from core.utils.constants import GENDER_CHOICES, STATUS_CHOICES, URL_MAX_LENGTH
from core.utils.validators import validate_nik


class Participant(TimeStampedModel):
    name = models.CharField(max_length=100)
    stage_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    nik = models.CharField(max_length=16, unique=True, validators=[validate_nik])
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    whatsapp = models.CharField(max_length=20)
    photo_close = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    photo_selfie = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    instagram = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    tiktok = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    facebook = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    region = models.CharField(max_length=100)
    invoice = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="registered"
    )

    def __str__(self):
        return f"{self.stage_name} - {self.name}"
