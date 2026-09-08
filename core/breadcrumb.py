from django.urls import reverse


def get_breadcrumb_context(request):
    url_name = request.resolver_match.url_name if request.resolver_match else ""
    breadcrumbs_map = {
        "index": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Dashboard", "url": "#", "active": True},
        ],
        "brand_summary": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Brand", "url": reverse("core:brand_summary"), "active": False},
            {"label": "Ringkasan", "url": "#", "active": True},
        ],
        "brand_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Brand", "url": reverse("core:brand_summary"), "active": False},
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "brand_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Brand", "url": reverse("core:brand_summary"), "active": False},
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "ads_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Advertisement",
                "url": reverse("core:ads_list"),
                "active": False,
            },
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "ads_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Advertisement",
                "url": reverse("core:ads_list"),
                "active": False,
            },
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "ads_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Advertisement",
                "url": reverse("core:ads_list"),
                "active": False,
            },
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "category_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Category",
                "url": reverse("core:category_list"),
                "active": False,
            },
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "category_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Category",
                "url": reverse("core:category_list"),
                "active": False,
            },
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "category_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Category",
                "url": reverse("core:category_list"),
                "active": False,
            },
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "tag_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Tag", "url": reverse("core:tag_list"), "active": False},
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "tag_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Tag", "url": reverse("core:tag_list"), "active": False},
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "tag_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Tag", "url": reverse("core:tag_list"), "active": False},
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "page_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Page", "url": reverse("core:page_list"), "active": False},
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "page_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Page", "url": reverse("core:page_list"), "active": False},
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "page_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Page", "url": reverse("core:page_list"), "active": False},
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "article_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Article", "url": reverse("core:article_list"), "active": False},
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "article_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Article", "url": reverse("core:article_list"), "active": False},
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "article_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Article", "url": reverse("core:article_list"), "active": False},
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "configuration": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Syncronization",
                "url": reverse("core:configuration"),
                "active": False,
            },
            {"label": "Konfigurasi", "url": "#", "active": True},
        ],
        "carousel_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Carousel",
                "url": reverse("core:carousel_list"),
                "active": False,
            },
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "carousel_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Carousel",
                "url": reverse("core:carousel_list"),
                "active": False,
            },
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "carousel_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Carousel",
                "url": reverse("core:carousel_list"),
                "active": False,
            },
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "participant_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Participant",
                "url": reverse("core:participant_list"),
                "active": False,
            },
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "participant_detail": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Participant",
                "url": reverse("core:participant_list"),
                "active": False,
            },
            {"label": "Detail", "url": "#", "active": True},
        ],
        "participant_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Participant",
                "url": reverse("core:participant_list"),
                "active": False,
            },
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "participant_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {
                "label": "Participant",
                "url": reverse("core:participant_list"),
                "active": False,
            },
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "account_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Account", "url": reverse("core:account_list"), "active": False},
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "account_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Account", "url": reverse("core:account_list"), "active": False},
            {"label": "Tambah", "url": "#", "active": True},
        ],
        "account_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Account", "url": reverse("core:account_list"), "active": False},
            {"label": "Perbarui", "url": "#", "active": True},
        ],
        "album_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Gallery", "url": reverse("core:album_list"), "active": False},
            {"label": "Album", "url": "#", "active": True},
        ],
        "album_create": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Gallery", "url": reverse("core:album_list"), "active": False},
            {"label": "Tambah Album", "url": "#", "active": True},
        ],
        "album_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Gallery", "url": reverse("core:album_list"), "active": False},
            {"label": "Perbarui Album", "url": "#", "active": True},
        ],
        "photo_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Gallery", "url": reverse("core:album_list"), "active": False},
            {"label": "Photos", "url": "#", "active": True},
        ],
        "comment_list": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Comments", "url": reverse("core:comment_list"), "active": False},
            {"label": "Daftar", "url": "#", "active": True},
        ],
        "comment_update": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Comments", "url": reverse("core:comment_list"), "active": False},
            {"label": "Ubah Status", "url": "#", "active": True},
        ],
        "comment_delete": [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Comments", "url": reverse("core:comment_list"), "active": False},
            {"label": "Hapus", "url": "#", "active": True},
        ],
    }
    return breadcrumbs_map.get(
        url_name,
        [
            {"label": "Home", "url": reverse("core:index"), "active": False},
            {"label": "Dashboard", "url": "#", "active": True},
        ],
    )
