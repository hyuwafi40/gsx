from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Category, Tag, Article, Page, Album, Photos, Advertisement, Carousel


@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Tag)
@receiver(pre_save, sender=Article)
@receiver(pre_save, sender=Page)
@receiver(pre_save, sender=Album)
@receiver(pre_save, sender=Photos)
@receiver(pre_save, sender=Advertisement)
@receiver(pre_save, sender=Carousel)
def slugify_model(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = (
            slugify(instance.name)
            if hasattr(instance, "name")
            else slugify(instance.title)
        )
        unique_slug = base_slug
        num = 1
        while sender.objects.filter(slug=unique_slug).exclude(pk=instance.pk).exists():
            unique_slug = f"{base_slug}-{num}"
            num += 1
        instance.slug = unique_slug
