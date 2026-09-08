from django.urls import reverse
from core.utils.access import get_user_role


def get_sidebar_context(request):
    current_url_name = request.resolver_match.url_name if request.resolver_match else ""
    user_role = get_user_role(request.user)
    menu_categories = []

    if user_role in ["developer", "administrator", "reguler"]:
        home_items = [
            {
                "label": "Dashboard",
                "icon": "fa-chart-line",
                "url": reverse("core:index"),
                "active": current_url_name == "index",
            },
            {
                "label": "Participant",
                "icon": "fa-users",
                "url": reverse("core:participant_list"),
                "active": current_url_name
                in [
                    "participant_list",
                    "participant_create",
                    "participant_update",
                    "participant_detail",
                    "participant_delete",
                ],
            },
        ]

        if user_role in ["developer", "administrator"]:
            home_items.append(
                {
                    "label": "Add Article",
                    "icon": "fa-pen-to-square",
                    "url": reverse("core:article_create"),
                    "active": current_url_name == "article_create",
                }
            )

        menu_categories.append(
            {
                "title": "Home",
                "items": home_items,
            }
        )

    if user_role in ["developer", "administrator"]:
        menu_categories.append(
            {
                "title": "Configuration",
                "items": [
                    {
                        "label": "User",
                        "icon": "fa-user-gear",
                        "url": reverse("core:account_list"),
                        "active": current_url_name
                        in [
                            "account_list",
                            "account_create",
                            "account_update",
                            "account_delete",
                        ],
                    },
                    {
                        "label": "Brand",
                        "icon": "fa-cube",
                        "url": reverse("core:brand_summary"),
                        "active": current_url_name
                        in ["brand_summary", "brand_create", "brand_update"],
                    },
                    {
                        "label": "Advertisement",
                        "icon": "fa-rectangle-ad",
                        "url": reverse("core:ads_list"),
                        "active": current_url_name
                        in ["ads_list", "ads_create", "ads_update", "ads_delete"],
                    },
                    {
                        "label": "Category",
                        "icon": "fa-layer-group",
                        "url": reverse("core:category_list"),
                        "active": current_url_name
                        in [
                            "category_list",
                            "category_create",
                            "category_update",
                            "category_delete",
                        ],
                    },
                    {
                        "label": "Tag",
                        "icon": "fa-tags",
                        "url": reverse("core:tag_list"),
                        "active": current_url_name
                        in ["tag_list", "tag_create", "tag_update", "tag_delete"],
                    },
                    {
                        "label": "Syncronization",
                        "icon": "fa-plug",
                        "url": reverse("core:configuration"),
                        "active": current_url_name in ["configuration", "webhook"],
                    },
                ],
            }
        )

        menu_categories.append(
            {
                "title": "Management",
                "items": [
                    {
                        "label": "Page",
                        "icon": "fa-file",
                        "url": reverse("core:page_list"),
                        "active": current_url_name
                        in ["page_list", "page_create", "page_update", "page_delete"],
                    },
                    {
                        "label": "Article",
                        "icon": "fa-newspaper",
                        "url": reverse("core:article_list"),
                        "active": current_url_name
                        in [
                            "article_list",
                            "article_create",
                            "article_update",
                            "article_delete",
                        ],
                    },
                    {
                        "label": "Gallery",
                        "icon": "fa-images",
                        "url": reverse("core:album_list"),
                        "active": current_url_name
                        in [
                            "album_list",
                            "album_create",
                            "album_update",
                            "album_delete",
                            "photo_list",
                        ],
                    },
                    {
                        "label": "Carousel",
                        "icon": "fa-clapperboard",
                        "url": reverse("core:carousel_list"),
                        "active": current_url_name
                        in [
                            "carousel_list",
                            "carousel_create",
                            "carousel_update",
                            "carousel_delete",
                        ],
                    },
                    {
                        "label": "Comments",
                        "icon": "fa-comments",
                        "url": reverse("core:comment_list"),
                        "active": current_url_name
                        in ["comment_list", "comment_update", "comment_delete"],
                    },
                ],
            }
        )

    user_data = {
        "is_authenticated": request.user.is_authenticated,
        "full_name": (
            request.user.get_full_name() or request.user.username
            if request.user.is_authenticated
            else "Guest"
        ),
        "initials": (
            (request.user.get_full_name() or request.user.username)[:2].upper()
            if request.user.is_authenticated
            else "JD"
        ),
        "role": user_role.capitalize() if user_role else "Not Logged In",
    }

    return {
        "sidebar_menu_categories": menu_categories,
        "sidebar_user": user_data,
        "user_role": user_role,
    }
