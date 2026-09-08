from django.urls import reverse_lazy
from blog.models import Tag
from core.forms.tag import TagForm
from core.views.base import BaseDeleteView, BaseFormView, BaseListView
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER


class TagListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Tag
    search_fields = ["name"]
    template_name = "core/tag.html"
    partial_template_name = "core/tag/table.html"
    pagination_target = "#tagTableContainer"


class TagFormView(BaseFormView):
    model = Tag
    form_class = TagForm
    template_name = "core/tag.html"
    partial_template_name = "core/tag/form.html"
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    success_url = reverse_lazy("core:tag_list")


class TagCreateView(TagFormView):
    form_action = reverse_lazy("core:tag_create")
    success_message = "Tag berhasil dibuat."


class TagUpdateView(TagFormView):
    success_message = "Tag berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy("core:tag_update", kwargs={"pk": self.kwargs.get("pk")})


class TagDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Tag
    success_message = "Tag berhasil dihapus."
    success_url = reverse_lazy("core:tag_list")
