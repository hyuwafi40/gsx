from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from blog.forms import CommentForm
from blog.models import Article, Comment
from blog.services import get_ad_by_type


class ArticleListView(View):
    template_name = "blog/article/list.html"
    paginate_by = 10

    def get(self, request):
        articles = (
            Article.objects.filter(status="published")
            .select_related("category")
            .prefetch_related("tag")
        )
        query = request.GET.get("q", "")
        if query:
            articles = articles.filter(title__icontains=query)
        category = request.GET.get("category")
        if category:
            articles = articles.filter(category__slug=category)
        paginator = Paginator(articles, self.paginate_by)
        page_obj = paginator.get_page(request.GET.get("page"))

        context = {
            "page_obj": page_obj,
            "query": query,
            "leaderboard_ad": get_ad_by_type("leaderboard"),
            "native_ad": get_ad_by_type("native"),
            "mobile_banner_ad": get_ad_by_type("mobile_banner"),
            "pagination_target": "#articleListContainer",
        }
        if request.htmx:
            return render(request, "blog/article/content.html", context)
        return render(request, self.template_name, context)


class ArticleDetailView(View):
    template_name = "blog/article/detail.html"

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug, status="published")
        comments = Comment.objects.filter(article=article, status="approved").order_by(
            "-created_at"
        )
        form = CommentForm()
        context = {
            "article": article,
            "comments": comments,
            "form": form,
            "rectangle_ad": get_ad_by_type("rectangle"),
            "banner_ad": get_ad_by_type("banner"),
            "mobile_banner_ad": get_ad_by_type("mobile_banner"),
        }
        return render(request, self.template_name, context)


class CommentCreateView(View):
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug, status="published")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.status = "pending"
            comment.save()
            if request.htmx:
                comments = Comment.objects.filter(
                    article=article, status="approved"
                ).order_by("-created_at")
                context = {
                    "article": article,
                    "comments": comments,
                    "form": CommentForm(),
                }
                response = render(request, "blog/article/comments.html", context)
                response["HX-Trigger"] = (
                    '{"showToast": {"message": "Komentar berhasil dikirim.", "type": "success"}}'
                )
                return response
            messages.success(request, "Komentar Anda sedang dimoderasi.")
            return redirect("blog:article_detail", slug=slug)

        if request.htmx:
            comments = Comment.objects.filter(
                article=article, status="approved"
            ).order_by("-created_at")
            context = {
                "article": article,
                "comments": comments,
                "form": form,
            }
            return render(request, "blog/article/comments.html", context)

        comments = Comment.objects.filter(article=article, status="approved").order_by(
            "-created_at"
        )
        context = {
            "article": article,
            "comments": comments,
            "form": form,
        }
        return render(request, "blog/article/detail.html", context)
