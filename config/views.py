from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("core:index")
        return render(request, "index.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Login berhasil.")
                return redirect("core:index")
            else:
                messages.error(request, "Akun tidak aktif.")
        else:
            messages.error(request, "Username atau password salah.")
        return render(request, "index.html")


def logout_view(request):
    logout(request)
    return redirect("login")
