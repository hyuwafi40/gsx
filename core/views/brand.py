from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from core.models import Brand
from core.forms.brand import BrandForm
from core.views.base import BaseNonModalFormView, RoleRequiredMixin
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR
import logging

logger = logging.getLogger(__name__)


class BrandSummaryView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    template_name = "core/brand.html"

    def get(self, request, *args, **kwargs):
        brand = Brand.objects.first()
        context = {
            "brand": brand,
        }
        return render(request, self.template_name, context)


class BrandFormView(BaseNonModalFormView):
    model = Brand
    form_class = BrandForm
    template_name = "core/brand/form.html"
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    success_url = reverse_lazy("core:brand_summary")

    def get_object(self):
        return Brand.objects.first()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if isinstance(self, BrandCreateView) and self.object:
            return redirect("core:brand_update")
        if isinstance(self, BrandUpdateView) and not self.object:
            return redirect("core:brand_create")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if isinstance(self, BrandCreateView) and self.object:
            return redirect("core:brand_update")
        if isinstance(self, BrandUpdateView) and not self.object:
            return redirect("core:brand_create")
        return super().post(request, *args, **kwargs)


class BrandCreateView(BrandFormView):
    form_action = reverse_lazy("core:brand_create")
    success_message = "Brand berhasil dibuat."


class BrandUpdateView(BrandFormView):
    form_action = reverse_lazy("core:brand_update")
    success_message = "Brand berhasil diperbarui."
