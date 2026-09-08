from django.db.models import Count, Q
from django.views.generic import TemplateView
from core.models import Participant
from blog.models import (
    Article,
    Page,
    Category,
    Tag,
    Album,
    Photos,
    Advertisement,
    Comment,
)
from core.views.base import RoleRequiredMixin
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER


class IndexViews(RoleRequiredMixin, TemplateView):
    template_name = "core/index.html"
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        participant_stats = Participant.objects.aggregate(
            total=Count("id"),
            verified=Count("id", filter=Q(status="verified")),
            registered=Count("id", filter=Q(status="registered")),
        )
        article_stats = Article.objects.aggregate(
            total=Count("id"),
            published=Count("id", filter=Q(status="published")),
            draft=Count("id", filter=Q(status="draft")),
        )
        page_stats = Page.objects.aggregate(
            total=Count("id"),
            published=Count("id", filter=Q(status="published")),
        )
        comment_stats = Comment.objects.aggregate(
            total=Count("id"),
            pending=Count("id", filter=Q(status="pending")),
            approved=Count("id", filter=Q(status="approved")),
        )

        stats_cards = [
            {
                "label": "Participant",
                "value": participant_stats["total"],
                "icon": "fa-users",
                "icon_class": "stat-icon-blue",
                "changes": [
                    {
                        "icon": "fa-user-check",
                        "text": f"Terverifikasi: {participant_stats['verified']}",
                        "class": "change-up",
                    },
                    {
                        "icon": "fa-user-clock",
                        "text": f"Terdaftar: {participant_stats['registered']}",
                        "class": "change-down",
                    },
                ],
            },
            {
                "label": "Article",
                "value": article_stats["total"],
                "icon": "fa-newspaper",
                "icon_class": "stat-icon-green",
                "changes": [
                    {
                        "icon": "fa-check-circle",
                        "text": f"Published: {article_stats['published']}",
                        "class": "change-up",
                    },
                    {
                        "icon": "fa-edit",
                        "text": f"Draft: {article_stats['draft']}",
                        "class": "change-down",
                    },
                ],
            },
            {
                "label": "Page",
                "value": page_stats["total"],
                "icon": "fa-file",
                "icon_class": "stat-icon-orange",
                "changes": [
                    {
                        "icon": "fa-check-circle",
                        "text": f"Published: {page_stats['published']}",
                        "class": "change-up",
                    },
                ],
            },
            {
                "label": "Comments",
                "value": comment_stats["total"],
                "icon": "fa-comments",
                "icon_class": "stat-icon-red",
                "changes": [
                    {
                        "icon": "fa-check",
                        "text": f"Approved: {comment_stats['approved']}",
                        "class": "change-up",
                    },
                    {
                        "icon": "fa-clock",
                        "text": f"Pending: {comment_stats['pending']}",
                        "class": "change-down",
                    },
                ],
            },
            {
                "label": "Categories",
                "value": Category.objects.count(),
                "icon": "fa-layer-group",
                "icon_class": "stat-icon-blue",
                "changes": [],
            },
            {
                "label": "Tags",
                "value": Tag.objects.count(),
                "icon": "fa-tags",
                "icon_class": "stat-icon-green",
                "changes": [],
            },
            {
                "label": "Albums",
                "value": Album.objects.count(),
                "icon": "fa-images",
                "icon_class": "stat-icon-orange",
                "changes": [
                    {
                        "icon": "fa-camera",
                        "text": f"Photos: {Photos.objects.count()}",
                        "class": "change-up",
                    }
                ],
            },
            {
                "label": "Advertisements",
                "value": Advertisement.objects.count(),
                "icon": "fa-rectangle-ad",
                "icon_class": "stat-icon-red",
                "changes": [
                    {
                        "icon": "fa-play",
                        "text": f"Active: {Advertisement.objects.filter(status=True).count()}",
                        "class": "change-up",
                    }
                ],
            },
        ]

        context.update(
            {
                "stats_cards": stats_cards,
                "recent_participants": Participant.objects.order_by("-created_at")[:5],
                "recent_articles": Article.objects.order_by("-created_at")[:5],
            }
        )
        return context
