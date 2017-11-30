from imager_images.models import Photo, Album
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

# Create your views here.


class PhotoForm(CreateView):
    """Create instance of PhotoForm object."""
    model = Photo
    exclude = []
    template_name = 'imager_profile/create_photo.html'
    fields = ('title', 'image', 'description', 'published')
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


class AlbumForm(CreateView):
    """Create instance of AlbumForm object."""
    model = Album
    exclude = ['user', 'date_published']
    template_name = 'imager_profile/create_album.html'
    fields = ('photos', 'cover', 'title', 'description', 'published')
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


class LibraryView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'imager_profile/library.html'

    def get_object(self):
        return User.objects.get(username=self.request.user.username)