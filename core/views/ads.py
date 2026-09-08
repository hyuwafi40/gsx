from django.urls import reverse_lazy
from blog.models import Advertisement
from core.forms.ads import AdsForm
from core.views.base import BaseDeleteView, BaseFormView, BaseListView
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER


class AdsListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Advertisement
    search_fields = ["name"]
    template_name = "core/ads.html"
    partial_template_name = "core/ads/table.html"
    pagination_target = "#adsTableContainer"


class AdsFormView(BaseFormView):
    model = Advertisement
    form_class = AdsForm
    template_name = "core/ads.html"
    partial_template_name = "core/ads/form.html"
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    success_url = reverse_lazy("core:ads_list")


class AdsCreateView(AdsFormView):
    form_action = reverse_lazy("core:ads_create")
    success_message = "Iklan berhasil dibuat."


class AdsUpdateView(AdsFormView):
    success_message = "Iklan berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy("core:ads_update", kwargs={"pk": self.kwargs.get("pk")})


class AdsDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Advertisement
    success_message = "Iklan berhasil dihapus."
    success_url = reverse_lazy("core:ads_list")
