from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views import View
from xhtml2pdf import pisa
from core.models import Brand, Participant


class ParticipantListView(View):
    template_name = "blog/participant.html"
    paginate_by = 10

    def get(self, request):
        stats = Participant.objects.aggregate(
            total=Count("id"),
            registered=Count("id", filter=Q(status="registered")),
            verified=Count("id", filter=Q(status="verified")),
        )
        all_participants = Participant.objects.all().order_by("-updated_at")
        paginator = Paginator(all_participants, self.paginate_by)
        page_obj = paginator.get_page(request.GET.get("page"))

        context = {
            "stats": stats,
            "page_obj": page_obj,
            "pagination_target": "#participantTableContainer",
        }
        if request.htmx:
            return render(request, "blog/participant/table.html", context)
        return render(request, self.template_name, context)


class ParticipantSearchView(View):
    template_name = "blog/participant/search.html"
    paginate_by = 10

    def get(self, request):
        query = request.GET.get("q", "").strip()
        participants = Participant.objects.none()

        if query:
            participants = Participant.objects.filter(
                Q(stage_name__icontains=query)
                | Q(name__icontains=query)
                | Q(region__icontains=query)
            ).order_by("stage_name")
        else:
            participants = Participant.objects.none()

        paginator = Paginator(participants, self.paginate_by)
        page_obj = paginator.get_page(request.GET.get("page"))

        context = {
            "page_obj": page_obj,
            "query": query,
            "pagination_target": "#participantSearchResults",
        }
        if request.htmx:
            return render(request, "blog/participant/search_content.html", context)
        return render(request, self.template_name, context)


class ParticipantDetailView(View):
    template_name = "blog/participant/detail.html"

    def mask_value(self, value, mask_type):
        if not value:
            return "-"
        if mask_type == "nik":
            if len(str(value)) >= 4:
                return "**** **** **** " + str(value)[-4:]
            return "*" * len(str(value))
        if mask_type == "birthdate":
            if value:
                return "** ** " + str(value.year)[-2:]
            return "-"
        if mask_type == "email":
            if "@" in value:
                local, domain = value.split("@", 1)
                if len(local) > 2:
                    return local[0] + "***@" + domain
                return "***@" + domain
            return "***"
        if mask_type == "whatsapp":
            if len(value) > 4:
                return "***-***-" + value[-4:]
            return "***"
        return value

    def get(self, request, pk):
        participant = get_object_or_404(Participant, pk=pk, status="verified")
        brand = Brand.get_solo()
        context = {
            "participant": participant,
            "brand": brand,
            "masked_nik": self.mask_value(participant.nik, "nik"),
            "masked_birthdate": self.mask_value(participant.birthdate, "birthdate"),
            "masked_email": self.mask_value(participant.email, "email"),
            "masked_whatsapp": self.mask_value(participant.whatsapp, "whatsapp"),
        }
        return render(request, self.template_name, context)


class ParticipantDownloadView(View):
    def get(self, request, pk):
        participant = get_object_or_404(Participant, pk=pk, status="verified")
        brand = Brand.get_solo()
        context = {
            "participant": participant,
            "brand": brand,
            "masked_nik": self.mask_value(participant.nik, "nik"),
            "masked_birthdate": self.mask_value(participant.birthdate, "birthdate"),
            "masked_email": self.mask_value(participant.email, "email"),
            "masked_whatsapp": self.mask_value(participant.whatsapp, "whatsapp"),
        }
        html = render_to_string("blog/participant/pdf.html", context, request=request)
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = (
            f'attachment; filename="participant_{participant.pk}.pdf"'
        )
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            messages.error(request, "Gagal membuat PDF.")
            return redirect("blog:participant_detail", pk=pk)
        return response
