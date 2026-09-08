from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from config.views import LoginView, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("blog.urls", "blog"), namespace="blog")),
    path("core/", include(("core.urls", "core"), namespace="core")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
