from django.urls import reverse_lazy
from blog.models import Article
from core.forms.article import ArticleForm
from core.views.base import BaseDeleteView, BaseListView, BaseNonModalFormView
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER


class ArticleListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Article
    search_fields = ["title"]
    template_name = "core/article.html"
    partial_template_name = "core/article/table.html"
    pagination_target = "#articleTableContainer"

    def get_queryset(self):
        return super().get_queryset().select_related("category")


class ArticleCreateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Article
    form_class = ArticleForm
    template_name = "core/article/form.html"
    success_url = reverse_lazy("core:article_list")
    success_message = "Artikel berhasil dibuat."
    form_action = reverse_lazy("core:article_create")

    def save_form(self, form):
        article = form.save(commit=False)
        article.created_by = self.request.user
        article.save()
        form.save_m2m()
        return article


class ArticleUpdateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Article
    form_class = ArticleForm
    template_name = "core/article/form.html"
    success_url = reverse_lazy("core:article_list")
    success_message = "Artikel berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy("core:article_update", kwargs={"pk": self.kwargs.get("pk")})

    def save_form(self, form):
        article = form.save(commit=False)
        article.created_by = self.request.user
        article.save()
        form.save_m2m()
        return article


class ArticleDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Article
    success_message = "Artikel berhasil dihapus."
    success_url = reverse_lazy("core:article_list")
