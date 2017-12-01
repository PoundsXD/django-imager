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

<<<<<<< HEAD

class LibraryView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'imager_profile/library.html'

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


class SinglePhotoView(DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'imager_profile/single_photo.html'
=======
'''
class PhotoListView(ListView):
    model = Photo
    queryset = Photo.objects.order_by(some_value)
    context_object_name = 'objects'
    template_name = 'app/template.html'
    '''
>>>>>>> a564e29c03a26a2c70fe4345cbe1ef164d4699ad
