from datetime import datetime
from core.models import Brand
from blog.models import Page


def get_footer_context(request):
    brand = Brand.get_solo()
    pages = Page.objects.filter(status="published").order_by("title")

    return {
        "blog_current_year": datetime.now().year,
        "blog_brand_name": brand.name,
        "blog_brand_description": brand.description,
        "blog_social_links": {
            "facebook": brand.facebook,
            "instagram": brand.instagram,
            "tiktok": brand.tiktok,
            "youtube": brand.youtube,
        },
        "blog_footer_pages": pages,
    }
