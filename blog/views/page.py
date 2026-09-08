from django.shortcuts import get_object_or_404, render
from django.views import View
from blog.models import Page


class PageListView(View):
    template_name = "blog/page/list.html"

    def get(self, request):
        pages = Page.objects.filter(status="published").order_by("title")
        context = {
            "page_obj": pages,
        }
        return render(request, self.template_name, context)


class PageDetailView(View):
    template_name = "blog/page/detail.html"

    def get(self, request, slug):
        page = get_object_or_404(Page, slug=slug, status="published")
        context = {
            "page": page,
        }
        return render(request, self.template_name, context)
