from django.contrib import admin
from .models import (
    Category,
    Tag,
    Article,
    Page,
    Comment,
    Album,
    Photos,
    Advertisement,
    Carousel,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name",)
    readonly_fields = ("slug", "created_at", "updated_at")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name",)
    readonly_fields = ("slug", "created_at", "updated_at")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "is_important",
        "created_by_full_name",
        "created_at",
    )
    list_filter = ("status", "is_important", "category")
    search_fields = ("title", "content")
    filter_horizontal = ("tag",)
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    list_select_related = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_by_full_name", "created_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    list_select_related = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "article", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "email", "content")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_by_full_name", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "description")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    list_select_related = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ("name", "album", "created_by_full_name", "created_at")
    search_fields = ("name", "caption")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    list_select_related = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("name", "type_ads", "status", "end_date", "created_by_full_name")
    list_filter = ("status", "type_ads")
    search_fields = ("name",)
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    list_select_related = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("name", "ordering", "created_by_full_name", "created_at")
    list_editable = ("ordering",)
    search_fields = ("name",)
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    list_select_related = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
