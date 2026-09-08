from django.views.generic import TemplateView
from blog.services import (
    get_active_carousel,
    get_headline_articles,
    get_latest_articles,
)


class IndexViews(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "carousel_items": get_active_carousel(),
                "headline_articles": get_headline_articles(),
                "latest_articles": get_latest_articles(),
            }
        )
        return context
