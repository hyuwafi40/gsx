from django.urls import path
from blog.views.index import IndexViews
from blog.views.article import ArticleListView, ArticleDetailView, CommentCreateView
from blog.views.page import PageListView, PageDetailView
from blog.views.gallery import AlbumListView, PhotoListView, PhotoDetailView
from blog.views.participant import (
    ParticipantListView,
    ParticipantDetailView,
    ParticipantDownloadView,
    ParticipantSearchView,
)

app_name = "blog"

urlpatterns = [
    path("", IndexViews.as_view(), name="index"),
    path("a/", ArticleListView.as_view(), name="article_list"),
    path("a/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("a/<slug:slug>/c/", CommentCreateView.as_view(), name="comment_create"),
    path("p/", PageListView.as_view(), name="page_list"),
    path("p/<slug:slug>/", PageDetailView.as_view(), name="page_detail"),
    path("g/", AlbumListView.as_view(), name="album_list"),
    path("g/<slug:album_slug>/", PhotoListView.as_view(), name="photo_list"),
    path("g/<slug:album_slug>/<slug:photo_slug>/", PhotoDetailView.as_view(), name="photo_detail",),
    path("par/", ParticipantListView.as_view(), name="participant_list"),
    path("par/search/", ParticipantSearchView.as_view(), name="participant_search"),
    path("par/<int:pk>/", ParticipantDetailView.as_view(), name="participant_detail"),
    path("par/<int:pk>/download/", ParticipantDownloadView.as_view(), name="participant_download"),
]
