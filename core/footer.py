from datetime import datetime
from core.models import Brand


def get_footer_context(request):
    brand = Brand.get_solo()
    social_links = {
        "facebook": brand.facebook,
        "instagram": brand.instagram,
        "tiktok": brand.tiktok,
        "youtube": brand.youtube,
    }
    return {
        "current_year": datetime.now().year,
        "brand_name": brand.name,
        "social_links": social_links,
    }
