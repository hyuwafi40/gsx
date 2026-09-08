from core.models import Brand
from core.sidebar import get_sidebar_context
from core.navbar import get_navbar_context
from core.footer import get_footer_context
from core.breadcrumb import get_breadcrumb_context
from core.utils.access import get_user_role


def brand_info(request):
    return {"brand": Brand.get_solo()}


def global_partials(request):
    context = {}
    context.update(get_sidebar_context(request))
    context.update(get_navbar_context(request))
    context.update(get_footer_context(request))
    context["user_role"] = get_user_role(request.user)
    context["breadcrumbs"] = get_breadcrumb_context(request)
    return context
