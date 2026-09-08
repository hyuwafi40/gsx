from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from core.forms.account import AccountCreateForm, AccountUpdateForm
from core.views.base import BaseDeleteView, BaseListView, RoleRequiredMixin
from core.utils.access import get_user_role, apply_role_to_user
from core.utils.constants import (
    ACCOUNT_ROLE_CHOICES_LIMITED,
    ROLE_DEVELOPER,
    ROLE_ADMINISTRATOR,
)
import logging

logger = logging.getLogger(__name__)


class AccountListView(BaseListView):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    model = User
    search_fields = ["username", "email"]
    template_name = "core/account.html"
    partial_template_name = "core/account/table.html"
    pagination_target = "#accountTableContainer"


class AccountCreateView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    template_name = "core/account/form.html"

    def get(self, request, *args, **kwargs):
        form = AccountCreateForm()
        context = {"form": form, "form_action": reverse_lazy("core:account_create")}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data.get("password1"))
                role = form.cleaned_data.get("role")
                apply_role_to_user(user, role)
                user.save()
                messages.success(request, "Akun berhasil dibuat.")
                return redirect("core:account_list")
            except Exception:
                logger.exception("Error creating account")
                messages.error(request, "Terjadi kesalahan saat membuat akun.")
        context = {"form": form, "form_action": reverse_lazy("core:account_create")}
        return render(request, self.template_name, context)


class AccountUpdateView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER, ROLE_ADMINISTRATOR]
    template_name = "core/account/form.html"

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get("pk"))
        initial = {
            "role": (
                get_user_role(user)
                if get_user_role(user) in dict(ACCOUNT_ROLE_CHOICES_LIMITED).keys()
                else "nonactive"
            )
        }
        form = AccountUpdateForm(instance=user, initial=initial)
        if user.is_superuser:
            form.fields["role"].widget.attrs["disabled"] = True
            form.fields["role"].required = False
        context = {
            "form": form,
            "form_action": reverse_lazy("core:account_update", kwargs={"pk": user.pk}),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get("pk"))
        form = AccountUpdateForm(request.POST, instance=user)
        if user.is_superuser:
            form.fields["role"].widget.attrs["disabled"] = True
            form.fields["role"].required = False
        if form.is_valid():
            try:
                user = form.save(commit=False)
                password = form.cleaned_data.get("password")
                if password:
                    user.set_password(password)
                if not user.is_superuser:
                    role = form.cleaned_data.get("role")
                    apply_role_to_user(user, role)
                user.save()
                messages.success(request, "Akun berhasil diperbarui.")
                return redirect("core:account_list")
            except Exception:
                logger.exception("Error updating account")
                messages.error(request, "Terjadi kesalahan saat memperbarui akun.")
        context = {
            "form": form,
            "form_action": reverse_lazy("core:account_update", kwargs={"pk": user.pk}),
        }
        return render(request, self.template_name, context)


class AccountDeleteView(BaseDeleteView):
    allowed_roles = [ROLE_DEVELOPER]
    model = User
    success_message = "Akun berhasil dihapus."
    success_url = reverse_lazy("core:account_list")

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get("pk"))
        if user == request.user:
            messages.error(request, "Anda tidak dapat menghapus akun sendiri.")
            return redirect("core:account_list")
        if user.is_superuser and User.objects.filter(is_superuser=True).count() <= 1:
            messages.error(request, "Tidak dapat menghapus superuser terakhir.")
            return redirect("core:account_list")
        return super().post(request, *args, **kwargs)


class AccountRoleUpdateView(RoleRequiredMixin, View):
    allowed_roles = [ROLE_DEVELOPER]

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get("pk"))
        if user.is_superuser:
            return render(
                request,
                "core/account/role.html",
                {"account": user, "user_role": get_user_role(request.user)},
            )
        role = request.POST.get("role")
        if role not in dict(ACCOUNT_ROLE_CHOICES_LIMITED).keys():
            return render(
                request,
                "core/account/role.html",
                {"account": user, "user_role": get_user_role(request.user)},
            )
        apply_role_to_user(user, role)
        try:
            user.save()
            response = render(
                request,
                "core/account/role.html",
                {"account": user, "user_role": get_user_role(request.user)},
            )
            response["HX-Trigger"] = (
                '{"showToast": {"message": "Role berhasil diperbarui", "type": "success"}}'
            )
            return response
        except Exception:
            logger.exception("Error updating role")
            return render(
                request,
                "core/account/role.html",
                {"account": user, "user_role": get_user_role(request.user)},
            )
