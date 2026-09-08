import json
import logging

from django.conf import settings
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from core.models import Participant
from core.utils.synchronization import upsert_participant_from_data
from core.views.base import RoleRequiredMixin
from core.utils.constants import ROLE_DEVELOPER, ROLE_ADMINISTRATOR

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class WebhookView(View):
    def post(self, request):
        token = request.headers.get("X-API-Token", "")
        if token != settings.APP_SCRIPT_TOKEN:
            return JsonResponse(
                {"status": "error", "message": "Token tidak valid"}, status=403
            )

        try:
            data = json.loads(request.body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse(
                {"status": "error", "message": "JSON tidak valid"}, status=400
            )

        if not isinstance(data, dict):
            return JsonResponse(
                {"status": "error", "message": "Format data harus object"}, status=400
            )

        try:
            participant, created = upsert_participant_from_data(data)
            message = "created" if created else "updated"
            return JsonResponse(
                {
                    "status": "success",
                    "message": message,
                    "participant_id": participant.id,
                },
                status=200,
            )
        except ValueError as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        except Exception:
            logger.exception("Webhook participant sync error")
            return JsonResponse(
                {"status": "error", "message": "Terjadi kesalahan server"}, status=500
            )


class ConfigurationView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    template_name = "core/configuration.html"

    def get(self, request):
        stats = Participant.objects.aggregate(
            total=Count("id"),
            registered=Count("id", filter=Q(status="registered")),
            verified=Count("id", filter=Q(status="verified")),
        )
        context = {
            "menu_items": [
                {
                    "label": "Webhook Google Apps Script",
                    "icon": "fa-plug",
                    "url": "#",
                    "active": True,
                },
            ],
            "stats": stats,
            "last_checked": timezone.now(),
        }
        return render(request, self.template_name, context)
