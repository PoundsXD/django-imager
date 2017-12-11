from django.contrib import admin

# Register your models here.
from imager_images.models import Photo
from imager_images.models import Album

admin.site.register(Photo)
admin.site.register(Album)