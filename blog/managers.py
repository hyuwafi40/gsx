from django.db import models


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class ApprovedCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="approved")


class ActiveAdvertisementManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)
