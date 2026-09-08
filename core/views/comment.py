from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views import View
from blog.models import Comment
from blog.constants import COMMENT_STATUS_CHOICES
from core.views.base import BaseDeleteView, BaseListView, RoleRequiredMixin
from core.utils.access import get_user_role
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR
import logging

logger = logging.getLogger(__name__)


class CommentListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Comment
    search_fields = ["content", "name", "email", "article__title"]
    template_name = "core/comment.html"
    partial_template_name = "core/comment/table.html"
    paginate_by = 10
    pagination_target = "#commentTableContainer"

    def get_queryset(self):
        return super().get_queryset().select_related("article")


class CommentStatusUpdateView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get("pk"))
        status = request.POST.get("status")
        valid_statuses = {choice[0] for choice in COMMENT_STATUS_CHOICES}
        if status not in valid_statuses:
            return render(
                request,
                "core/comment/status.html",
                {"comment": comment, "user_role": get_user_role(request.user)},
            )
        try:
            comment.status = status
            comment.save()
            response = render(
                request,
                "core/comment/status.html",
                {"comment": comment, "user_role": get_user_role(request.user)},
            )
            response["HX-Trigger"] = (
                '{"showToast": {"message": "Status komentar diperbarui", "type": "success"}}'
            )
            return response
        except Exception:
            logger.exception("Error updating comment status")
            return render(
                request,
                "core/comment/status.html",
                {"comment": comment, "user_role": get_user_role(request.user)},
            )


class CommentDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Comment
    success_message = "Komentar berhasil dihapus."
    success_url = None

    def get_success_url(self):
        from django.urls import reverse_lazy

        return reverse_lazy("core:comment_list")
