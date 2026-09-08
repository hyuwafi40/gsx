from django.urls import reverse_lazy
from blog.models import Carousel
from core.forms.carousel import CarouselForm
from core.views.base import BaseDeleteView, BaseFormView, BaseListView
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER


class CarouselListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Carousel
    search_fields = ["name"]
    template_name = "core/carousel.html"
    partial_template_name = "core/carousel/table.html"
    pagination_target = "#carouselTableContainer"


class CarouselFormView(BaseFormView):
    model = Carousel
    form_class = CarouselForm
    template_name = "core/carousel.html"
    partial_template_name = "core/carousel/form.html"
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    success_url = reverse_lazy("core:carousel_list")


class CarouselCreateView(CarouselFormView):
    form_action = reverse_lazy("core:carousel_create")
    success_message = "Carousel berhasil dibuat."


class CarouselUpdateView(CarouselFormView):
    success_message = "Carousel berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy(
            "core:carousel_update", kwargs={"pk": self.kwargs.get("pk")}
        )


class CarouselDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Carousel
    success_message = "Carousel berhasil dihapus."
    success_url = reverse_lazy("core:carousel_list")
