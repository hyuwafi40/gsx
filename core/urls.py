from django.urls import path
from core.views.index import IndexViews
from core.views.brand import BrandSummaryView, BrandCreateView, BrandUpdateView
from core.views.ads import AdsListView, AdsCreateView, AdsUpdateView, AdsDeleteView
from core.views.category import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
from core.views.tag import TagListView, TagCreateView, TagUpdateView, TagDeleteView
from core.views.page import PageListView, PageCreateView, PageUpdateView, PageDeleteView
from core.views.article import (
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)
from core.views.carousel import (
    CarouselListView,
    CarouselCreateView,
    CarouselUpdateView,
    CarouselDeleteView,
)
from core.views.participant import (
    ParticipantListView,
    ParticipantDetailView,
    ParticipantCreateView,
    ParticipantUpdateView,
    ParticipantDeleteView,
    ParticipantStatusUpdateView,
)
from core.views.account import (
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    AccountRoleUpdateView,
)
from core.views.gallery import (
    AlbumListView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
    AlbumStatusUpdateView,
    PhotoListView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
)
from core.views.comment import (
    CommentListView,
    CommentStatusUpdateView,
    CommentDeleteView,
)
from core.views.hook import WebhookView, ConfigurationView

app_name = "core"

urlpatterns = [
    path("", IndexViews.as_view(), name="index"),
    path("br/", BrandSummaryView.as_view(), name="brand_summary"),
    path("br/cre/", BrandCreateView.as_view(), name="brand_create"),
    path("br/upd/", BrandUpdateView.as_view(), name="brand_update"),
    path("ads/", AdsListView.as_view(), name="ads_list"),
    path("ads/cre/", AdsCreateView.as_view(), name="ads_create"),
    path("ads/upd/<int:pk>/", AdsUpdateView.as_view(), name="ads_update"),
    path("ads/del/<int:pk>/", AdsDeleteView.as_view(), name="ads_delete"),
    path("ct/", CategoryListView.as_view(), name="category_list"),
    path("ct/cre/", CategoryCreateView.as_view(), name="category_create"),
    path("ct/upd/<int:pk>/", CategoryUpdateView.as_view(), name="category_update"),
    path("ct/del/<int:pk>/", CategoryDeleteView.as_view(), name="category_delete"),
    path("tg/", TagListView.as_view(), name="tag_list"),
    path("tg/cre/", TagCreateView.as_view(), name="tag_create"),
    path("tg/upd/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tg/del/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
    path("pg/", PageListView.as_view(), name="page_list"),
    path("pg/cre/", PageCreateView.as_view(), name="page_create"),
    path("pg/upd/<int:pk>/", PageUpdateView.as_view(), name="page_update"),
    path("pg/del/<int:pk>/", PageDeleteView.as_view(), name="page_delete"),
    path("ar/", ArticleListView.as_view(), name="article_list"),
    path("ar/cre/", ArticleCreateView.as_view(), name="article_create"),
    path("ar/upd/<int:pk>/", ArticleUpdateView.as_view(), name="article_update"),
    path("ar/del/<int:pk>/", ArticleDeleteView.as_view(), name="article_delete"),
    path("cs/", CarouselListView.as_view(), name="carousel_list"),
    path("cs/cre/", CarouselCreateView.as_view(), name="carousel_create"),
    path("cs/upd/<int:pk>/", CarouselUpdateView.as_view(), name="carousel_update"),
    path("cs/del/<int:pk>/", CarouselDeleteView.as_view(), name="carousel_delete"),
    path("pa/", ParticipantListView.as_view(), name="participant_list"),
    path("pa/det/<int:pk>/", ParticipantDetailView.as_view(), name="participant_detail"),
    path("pa/cre/", ParticipantCreateView.as_view(), name="participant_create"),
    path("pa/upd/<int:pk>/", ParticipantUpdateView.as_view(), name="participant_update"),
    path("pa/del/<int:pk>/", ParticipantDeleteView.as_view(), name="participant_delete"),
    path("pa/st/<int:pk>/",ParticipantStatusUpdateView.as_view(), name="participant_status_update"),
    path("us/", AccountListView.as_view(), name="account_list"),
    path("us/cre/", AccountCreateView.as_view(), name="account_create"),
    path("us/upd/<int:pk>/", AccountUpdateView.as_view(), name="account_update"),
    path("us/del/<int:pk>/", AccountDeleteView.as_view(), name="account_delete"),
    path("us/rl/<int:pk>/", AccountRoleUpdateView.as_view(), name="account_role_update"),
    path("al/", AlbumListView.as_view(), name="album_list"),
    path("al/cre/", AlbumCreateView.as_view(), name="album_create"),
    path("al/upd/<int:pk>/", AlbumUpdateView.as_view(), name="album_update"),
    path("al/del/<int:pk>/", AlbumDeleteView.as_view(), name="album_delete"),
    path("al/st/<int:pk>/", AlbumStatusUpdateView.as_view(), name="album_status_update"),
    path("al/<int:album_pk>/ph/", PhotoListView.as_view(), name="photo_list"),
    path("al/<int:album_pk>/ph/cre/", PhotoCreateView.as_view(), name="photo_create"),
    path("al/ph/upd/<int:pk>/", PhotoUpdateView.as_view(), name="photo_update"),
    path("al/ph/del/<int:pk>/", PhotoDeleteView.as_view(), name="photo_delete"),
    path("cm/", CommentListView.as_view(), name="comment_list"),
    path("cm/upd/<int:pk>/", CommentStatusUpdateView.as_view(), name="comment_update"),
    path("cm/del/<int:pk>/", CommentDeleteView.as_view(), name="comment_delete"),
    path("sync/", ConfigurationView.as_view(), name="configuration"),
    path("hook/", WebhookView.as_view(), name="webhook"),
]
