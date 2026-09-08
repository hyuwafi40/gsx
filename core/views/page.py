from django.urls import reverse_lazy
from blog.models import Page
from core.forms.page import PageForm
from core.views.base import BaseDeleteView, BaseListView, BaseNonModalFormView
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER


class PageListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Page
    search_fields = ["title"]
    template_name = "core/page.html"
    partial_template_name = "core/page/table.html"
    pagination_target = "#pageTableContainer"


class PageCreateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Page
    form_class = PageForm
    template_name = "core/page/form.html"
    success_url = reverse_lazy("core:page_list")
    success_message = "Halaman berhasil dibuat."
    form_action = reverse_lazy("core:page_create")

    def save_form(self, form):
        page = form.save(commit=False)
        page.created_by = self.request.user
        page.save()
        return page


class PageUpdateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Page
    form_class = PageForm
    template_name = "core/page/form.html"
    success_url = reverse_lazy("core:page_list")
    success_message = "Halaman berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy("core:page_update", kwargs={"pk": self.kwargs.get("pk")})

    def save_form(self, form):
        page = form.save(commit=False)
        page.created_by = self.request.user
        page.save()
        return page


class PageDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Page
    success_message = "Halaman berhasil dihapus."
    success_url = reverse_lazy("core:page_list")
