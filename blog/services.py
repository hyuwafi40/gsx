from django.utils import timezone
from blog.models import Article, Advertisement, Carousel, Album


def get_published_articles():
    return Article.objects.filter(status="published")


def get_active_advertisements():
    return Advertisement.objects.filter(status=True, end_date__gte=timezone.now())


def get_published_albums():
    return Album.objects.filter(status="published")


def get_active_carousel():
    return Carousel.objects.all().order_by("ordering")


def get_ad_by_type(type_ads):
    return Advertisement.objects.filter(
        status=True,
        type_ads=type_ads,
        end_date__gte=timezone.now(),
    ).first()


def _published_articles():
    return Article.objects.filter(status="published").select_related("category")


def get_headline_articles():
    return _published_articles().filter(is_important=True).order_by("-created_at")[:5]


def get_latest_articles():
    return _published_articles().order_by("-created_at")[:6]
