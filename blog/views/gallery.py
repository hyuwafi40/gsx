from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views import View
from blog.models import Album, Photos


class AlbumListView(View):
    template_name = "blog/gallery/album.html"

    def get(self, request):
        albums = (
            Album.objects.filter(status="published")
            .annotate(photo_count=Count("photos"))
            .order_by("-created_at")
        )
        context = {
            "album_obj": albums,
        }
        return render(request, self.template_name, context)


class PhotoListView(View):
    template_name = "blog/gallery/photo.html"

    def get(self, request, album_slug):
        album = get_object_or_404(Album, slug=album_slug, status="published")
        photos = Photos.objects.filter(album=album).order_by("-created_at")
        context = {
            "album": album,
            "photo_obj": photos,
        }
        return render(request, self.template_name, context)


class PhotoDetailView(View):
    template_name = "blog/gallery/detail.html"

    def get(self, request, album_slug, photo_slug):
        album = get_object_or_404(Album, slug=album_slug, status="published")
        photo = get_object_or_404(Photos, slug=photo_slug, album=album)
        context = {
            "album": album,
            "photo": photo,
        }
        return render(request, self.template_name, context)
