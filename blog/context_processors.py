from blog.navbar import get_navbar_context
from blog.footer import get_footer_context


def global_blog_partials(request):
    context = {}
    context.update(get_navbar_context(request))
    context.update(get_footer_context(request))
    return context
