from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from blog.models import Album, Photos
from core.forms.gallery import AlbumForm, PhotoForm
from core.views.base import (
    BaseDeleteView,
    BaseListView,
    BaseNonModalFormView,
    RoleRequiredMixin,
)
from core.utils.access import get_user_role
from core.utils.constants import (
    ALBUM_STATUS_CHOICES,
    ROLE_DEVELOPER,
    ROLE_ADMINISTRATOR,
    ROLE_REGULER,
)
import logging

logger = logging.getLogger(__name__)


class AlbumListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Album
    search_fields = ["name", "description"]
    template_name = "core/gallery.html"
    partial_template_name = "core/gallery/table.html"
    pagination_target = "#albumTableContainer"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("photos")


class AlbumCreateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Album
    form_class = AlbumForm
    template_name = "core/gallery/form.html"
    success_url = reverse_lazy("core:album_list")
    success_message = "Album berhasil dibuat."
    form_action = reverse_lazy("core:album_create")

    def save_form(self, form):
        album = form.save(commit=False)
        album.created_by = self.request.user
        album.save()
        return album


class AlbumUpdateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Album
    form_class = AlbumForm
    template_name = "core/gallery/form.html"
    success_url = reverse_lazy("core:album_list")
    success_message = "Album berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy("core:album_update", kwargs={"pk": self.kwargs.get("pk")})

    def save_form(self, form):
        album = form.save(commit=False)
        album.created_by = self.request.user
        album.save()
        return album


class AlbumDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Album
    success_message = "Album berhasil dihapus."
    success_url = reverse_lazy("core:album_list")


class AlbumStatusUpdateView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]

    def post(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs.get("pk"))
        status = request.POST.get("status")
        if status not in dict(ALBUM_STATUS_CHOICES).keys():
            return render(
                request,
                "core/gallery/album_status.html",
                {"album": album, "user_role": get_user_role(request.user)},
            )
        album.status = status
        try:
            album.save()
            response = render(
                request,
                "core/gallery/album_status.html",
                {"album": album, "user_role": get_user_role(request.user)},
            )
            response["HX-Trigger"] = (
                '{"showToast": {"message": "Status album diperbarui", "type": "success"}}'
            )
            return response
        except Exception:
            logger.exception("Error updating album status")
            return render(
                request,
                "core/gallery/album_status.html",
                {"album": album, "user_role": get_user_role(request.user)},
            )


class PhotoListView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    template_name = "core/gallery/photo/main.html"
    paginate_by = 12

    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs.get("album_pk"))
        photos = Photos.objects.filter(album=album).order_by("-created_at")
        paginator = Paginator(photos, self.paginate_by)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "album": album,
            "page_obj": page_obj,
            "user_role": get_user_role(request.user),
            "pagination_target": "#photoGridContainer",
        }
        if request.htmx:
            return render(request, "core/gallery/photo/card.html", context)
        return render(request, self.template_name, context)


class PhotoCreateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Photos
    form_class = PhotoForm
    template_name = "core/gallery/photo/form.html"
    success_url = None

    def get_success_url(self, album_pk):
        return reverse_lazy("core:photo_list", kwargs={"album_pk": album_pk})

    def get_form_action(self):
        album_pk = self.kwargs.get("album_pk")
        return reverse_lazy("core:photo_create", kwargs={"album_pk": album_pk})

    def get_success_message(self):
        return "Foto berhasil ditambahkan."

    def save_form(self, form):
        album = get_object_or_404(Album, pk=self.kwargs.get("album_pk"))
        photo = form.save(commit=False)
        photo.album = album
        photo.created_by = self.request.user
        photo.save()
        return photo

    def post(self, request, *args, **kwargs):
        form = self.form_class(**self.get_form_kwargs())
        if form.is_valid():
            try:
                self.save_form(form)
                messages.success(request, self.get_success_message())
                return redirect(self.get_success_url(self.kwargs.get("album_pk")))
            except Exception:
                logger.exception("Error creating photo")
                messages.error(request, "Terjadi kesalahan saat menambah foto.")
        return render(request, self.template_name, self.get_context_data(form=form))


class PhotoUpdateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Photos
    form_class = PhotoForm
    template_name = "core/gallery/photo/form.html"
    success_url = None

    def get_success_url(self, album_pk):
        return reverse_lazy("core:photo_list", kwargs={"album_pk": album_pk})

    def get_form_action(self):
        return reverse_lazy("core:photo_update", kwargs={"pk": self.kwargs.get("pk")})

    def get_success_message(self):
        return "Foto berhasil diperbarui."

    def save_form(self, form):
        photo = form.save(commit=False)
        photo.created_by = self.request.user
        photo.save()
        return photo

    def post(self, request, *args, **kwargs):
        photo = self.get_object()
        form = self.form_class(**self.get_form_kwargs())
        if form.is_valid():
            try:
                self.save_form(form)
                messages.success(request, self.get_success_message())
                return redirect(self.get_success_url(photo.album.pk))
            except Exception:
                logger.exception("Error updating photo")
                messages.error(request, "Terjadi kesalahan saat memperbarui foto.")
        return render(request, self.template_name, self.get_context_data(form=form))


class PhotoDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Photos
    success_message = "Foto berhasil dihapus."

    def get_success_url(self):
        album_pk = self.kwargs.get("album_pk")
        if not album_pk:
            photo = get_object_or_404(Photos, pk=self.kwargs.get("pk"))
            album_pk = photo.album.pk
        return reverse_lazy("core:photo_list", kwargs={"album_pk": album_pk})
