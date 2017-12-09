from django.contrib import admin

# Register your models here.
from apps.gallery.models import Album, AlbumCategory, AlbumImage

admin.site.register(Album)
admin.site.register(AlbumCategory)
admin.site.register(AlbumImage)
