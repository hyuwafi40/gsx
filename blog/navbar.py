from django.urls import reverse
from core.models import Brand
from blog.models import Page


def get_navbar_context(request):
    brand = Brand.get_solo()
    menu_items = [
        {
            "label": "Beranda",
            "url": reverse("blog:index"),
            "active": request.resolver_match.url_name == "index",
        },
        {
            "label": "Berita",
            "url": reverse("blog:article_list"),
            "active": request.resolver_match.url_name == "article_list",
        },
        {
            "label": "Galeri",
            "url": reverse("blog:album_list"),
            "active": request.resolver_match.url_name
            in ["album_list", "photo_list", "photo_detail"],
        },
        {
            "label": "Peserta",
            "url": reverse("blog:participant_list"),
            "active": request.resolver_match.url_name
            in [
                "participant_list",
                "participant_detail",
                "participant_download",
                # "participant_search",
            ],
        },
        {
            "label": "Cari Peserta",
            "url": reverse("blog:participant_search"),
            "active": request.resolver_match.url_name == "participant_search",
        },
        {
            "label": "Daftar",
            "url": "https://forms.gle/qfS3iRQF8cXBVgEm8",
            "active": False,
            "external": True,
        },
    ]

    pages = Page.objects.filter(status="published").order_by("title")
    for page in pages:
        menu_items.append(
            {
                "label": page.title,
                "url": reverse("blog:page_detail", args=[page.slug]),
                "active": request.resolver_match.url_name == "page_detail"
                and request.resolver_match.kwargs.get("slug") == page.slug,
            }
        )

    return {
        "blog_nav_items": menu_items,
        "blog_brand_name": brand.name,
        "blog_brand_logo": brand.logo,
        "blog_registration_url": "https://forms.gle/qfS3iRQF8cXBVgEm8",
    }
