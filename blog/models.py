from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from blog.mixins import TimestampMixin, CreatedByMixin
from blog.constants import (
    ARTICLE_STATUS_CHOICES,
    COMMENT_STATUS_CHOICES,
    AD_TYPE_CHOICES,
)
from blog.managers import (
    PublishedArticleManager,
    ApprovedCommentManager,
    ActiveAdvertisementManager,
)


class Category(TimestampMixin):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, editable=False)

    def __str__(self):
        return self.name


class Tag(TimestampMixin):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, editable=False)

    def __str__(self):
        return self.name


class Article(TimestampMixin, CreatedByMixin):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, editable=False)
    thumbnail = models.URLField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="articles"
    )
    tag = models.ManyToManyField(Tag, related_name="articles", blank=True)
    content = CKEditor5Field()
    status = models.CharField(
        max_length=20, choices=ARTICLE_STATUS_CHOICES, default="draft"
    )
    is_important = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedArticleManager()

    def __str__(self):
        return self.title


class Page(TimestampMixin, CreatedByMixin):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, editable=False)
    content = CKEditor5Field()
    status = models.CharField(
        max_length=20, choices=ARTICLE_STATUS_CHOICES, default="draft"
    )

    def __str__(self):
        return self.title


class Comment(TimestampMixin):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    status = models.CharField(
        max_length=20, choices=COMMENT_STATUS_CHOICES, default="pending"
    )

    objects = models.Manager()
    approved = ApprovedCommentManager()

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"


class Album(TimestampMixin, CreatedByMixin):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    thumbnail = models.URLField(blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=ARTICLE_STATUS_CHOICES, default="draft"
    )

    def __str__(self):
        return self.name


class Photos(TimestampMixin, CreatedByMixin):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    image = models.URLField()
    caption = models.CharField(max_length=255, blank=True)
    album = models.ForeignKey(
        Album, on_delete=models.SET_NULL, null=True, blank=True, related_name="photos"
    )

    def __str__(self):
        return self.name


class Advertisement(TimestampMixin, CreatedByMixin):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    type_ads = models.CharField(max_length=30, choices=AD_TYPE_CHOICES)
    image = models.URLField()
    link = models.CharField(max_length=255)
    end_date = models.DateTimeField()
    status = models.BooleanField(default=True)

    objects = models.Manager()
    active = ActiveAdvertisementManager()

    def __str__(self):
        return self.name


class Carousel(TimestampMixin, CreatedByMixin):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, editable=False)
    image = models.URLField()
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordering"]

    def __str__(self):
        return self.name
