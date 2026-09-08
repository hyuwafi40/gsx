from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from core.utils.access import get_user_role
import logging

logger = logging.getLogger(__name__)


class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        user_role = get_user_role(request.user)
        if user_role not in self.allowed_roles:
            return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
        return super().dispatch(request, *args, **kwargs)


class BaseListView(RoleRequiredMixin, View):
    model = None
    search_fields = []
    template_name = None
    partial_template_name = None
    paginate_by = 10
    pagination_target = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.GET.get("q", "")
        if query and self.search_fields:
            q_objects = Q()
            for field in self.search_fields:
                q_objects |= Q(**{f"{field}__icontains": query})
            queryset = queryset.filter(q_objects)
        if not queryset.ordered:
            queryset = queryset.order_by("pk")
        return queryset

    def get_context_data(self, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
            "query": self.request.GET.get("q", ""),
            "user_role": get_user_role(self.request.user),
            "pagination_target": self.pagination_target,
        }
        context.update(kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if request.htmx:
            return render(request, self.partial_template_name, context)
        return render(request, self.template_name, context)


class BaseDeleteView(RoleRequiredMixin, View):
    model = None
    success_message = None
    success_url = None

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get("pk"))
        try:
            obj.delete()
            messages.success(request, self.success_message)
        except Exception:
            logger.exception(f"Error deleting {self.model.__name__}")
            messages.error(request, "Gagal menghapus data.")
        return redirect(self.get_success_url())


class BaseFormView(RoleRequiredMixin, View):
    model = None
    form_class = None
    template_name = None
    partial_template_name = None
    success_message = None
    success_url = None
    form_action = None

    def get_object(self):
        pk = self.kwargs.get("pk")
        if pk:
            return get_object_or_404(self.model, pk=pk)
        return None

    def get_form_kwargs(self):
        kwargs = {}
        if self.request.method == "POST":
            kwargs["data"] = self.request.POST
        if hasattr(self, "object") and self.object:
            kwargs["instance"] = self.object
        return kwargs

    def get_form_action(self):
        return self.form_action

    def get_context_data(self, **kwargs):
        context = {
            "form": self.form_class(**self.get_form_kwargs()),
            "form_action": self.get_form_action(),
            "show_form_modal": True,
        }
        context.update(kwargs)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if request.htmx:
            return render(request, self.partial_template_name, context)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not hasattr(self, "object"):
            self.object = self.get_object()
        form = self.form_class(**self.get_form_kwargs())
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                if hasattr(instance, "created_by") and request.user.is_authenticated:
                    instance.created_by = request.user
                instance.save()
                form.save_m2m()
                messages.success(request, self.success_message)
                return redirect(self.success_url)
            except Exception:
                logger.exception(f"Error saving {self.model.__name__}")
                messages.error(request, "Terjadi kesalahan saat menyimpan data.")
        return render(request, self.template_name, self.get_context_data(form=form))


class BaseNonModalFormView(RoleRequiredMixin, View):
    model = None
    form_class = None
    template_name = None
    success_url = None
    success_message = None
    form_action = None

    def get_object(self):
        pk = self.kwargs.get("pk")
        if pk:
            return get_object_or_404(self.model, pk=pk)
        return None

    def get_form_kwargs(self):
        kwargs = {}
        if self.request.method == "POST":
            kwargs["data"] = self.request.POST
        obj = self.get_object()
        if obj:
            kwargs["instance"] = obj
        return kwargs

    def get_form_action(self):
        return self.form_action

    def get_context_data(self, **kwargs):
        context = {
            "form": self.form_class(**self.get_form_kwargs()),
            "form_action": self.get_form_action(),
        }
        context.update(kwargs)
        return context

    def save_form(self, form):
        return form.save()

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(**self.get_form_kwargs())
        if form.is_valid():
            try:
                self.save_form(form)
                messages.success(request, self.success_message)
                return redirect(self.success_url)
            except Exception:
                logger.exception(f"Error saving {self.model.__name__}")
                messages.error(request, "Terjadi kesalahan saat menyimpan data.")
        return render(request, self.template_name, self.get_context_data(form=form))
