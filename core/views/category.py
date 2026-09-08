from django.urls import reverse_lazy
from blog.models import Category
from core.forms.category import CategoryForm
from core.views.base import BaseDeleteView, BaseFormView, BaseListView
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER


class CategoryListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Category
    search_fields = ["name"]
    template_name = "core/category.html"
    partial_template_name = "core/category/table.html"
    pagination_target = "#categoryTableContainer"


class CategoryFormView(BaseFormView):
    model = Category
    form_class = CategoryForm
    template_name = "core/category.html"
    partial_template_name = "core/category/form.html"
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    success_url = reverse_lazy("core:category_list")


class CategoryCreateView(CategoryFormView):
    form_action = reverse_lazy("core:category_create")
    success_message = "Kategori berhasil dibuat."


class CategoryUpdateView(CategoryFormView):
    success_message = "Kategori berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy(
            "core:category_update", kwargs={"pk": self.kwargs.get("pk")}
        )


class CategoryDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Category
    success_message = "Kategori berhasil dihapus."
    success_url = reverse_lazy("core:category_list")
