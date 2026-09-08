from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from core.models import Participant
from core.forms.participant import ParticipantForm
from core.views.base import (
    BaseDeleteView,
    BaseListView,
    BaseNonModalFormView,
    RoleRequiredMixin,
)
from core.utils.access import get_user_role
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER
import logging

logger = logging.getLogger(__name__)


class ParticipantListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    model = Participant
    search_fields = ["name", "stage_name", "email"]
    template_name = "core/participant.html"
    partial_template_name = "core/participant/table.html"
    pagination_target = "#participantTableContainer"


class ParticipantDetailView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR, ROLE_REGULER]
    template_name = "core/participant/summary.html"

    def get(self, request, *args, **kwargs):
        participant = get_object_or_404(Participant, pk=kwargs.get("pk"))
        return render(request, self.template_name, {"participant": participant})


class ParticipantCreateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Participant
    form_class = ParticipantForm
    template_name = "core/participant/form.html"
    success_url = reverse_lazy("core:participant_list")
    success_message = "Participant berhasil dibuat."
    form_action = reverse_lazy("core:participant_create")


class ParticipantUpdateView(BaseNonModalFormView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = Participant
    form_class = ParticipantForm
    template_name = "core/participant/form.html"
    success_url = reverse_lazy("core:participant_list")
    success_message = "Participant berhasil diperbarui."

    def get_form_action(self):
        return reverse_lazy(
            "core:participant_update", kwargs={"pk": self.kwargs.get("pk")}
        )


class ParticipantDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = Participant
    success_message = "Participant berhasil dihapus."
    success_url = reverse_lazy("core:participant_list")


class ParticipantStatusUpdateView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]

    def post(self, request, *args, **kwargs):
        participant = get_object_or_404(Participant, pk=kwargs.get("pk"))
        status = request.POST.get("status")
        if status not in {"registered", "verified"}:
            return render(
                request,
                "core/participant/status.html",
                {"participant": participant, "user_role": get_user_role(request.user)},
            )
        participant.status = status
        try:
            participant.save()
            response = render(
                request,
                "core/participant/status.html",
                {"participant": participant, "user_role": get_user_role(request.user)},
            )
            response["HX-Trigger"] = (
                '{"showToast": {"message": "Status berhasil diperbarui", "type": "success"}}'
            )
            return response
        except Exception:
            logger.exception("Error updating participant status")
            return render(
                request,
                "core/participant/status.html",
                {"participant": participant, "user_role": get_user_role(request.user)},
            )
