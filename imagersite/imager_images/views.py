from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import views as auth_views

# Create your views here.


class UpdateAlbum(UpdateView):
    """Update an existing Album."""

    model = Album
    template_name = 'imager_images/edit_album.html'
    exclude = ['date_published', 'date_created', 'date_modified', 'user']
    fields = ('published', 'photos', 'cover', 'title', 'description')
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateView, self).form_valid(form)


class PhotoForm(CreateView):
    """Create instance of PhotoForm object."""
    model = Photo
    exclude = []
    template_name = 'imager_images/create_photo.html'
    fields = ('title', 'image', 'description', 'published')
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


class AlbumForm(CreateView):
    """Create instance of AlbumForm object."""
    model = Album
    exclude = ['user', 'date_published']
    template_name = 'imager_images/create_album.html'
    fields = ('photos', 'cover', 'title', 'description', 'published')
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


class LibraryView(DetailView):
    """Create instance of LibraryView object."""
    model = User
    context_object_name = 'user'
    template_name = 'imager_images/library.html'

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


class SinglePhotoView(DetailView):
    """Create instance of SinglePhotoView object."""
    model = Photo
    context_object_name = 'photo'
    template_name = 'imager_images/single_photo.html'


class SingleAlbumView(DetailView):
    """Create instance of SingleAlbumView object."""
    model = Album
    context_object_name = 'album'
    template_name = 'imager_images/single_album.html'


class OneProfileView(DetailView):
    """Create instance of OneProfileView object."""
    model = ImagerProfile
    context_object_name = 'profile'
    template_name = 'imager_profile/profile.html'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'


class PublicPhotosView(DetailView):
    """Create instance of PublicPhotosView object."""
    model = User
    context_object_name = 'public_photos'
    template_name = 'imager_images/public_photos.html'

    def get_object(self):
        return self.request.user.photo_set.filter(published='PUBLIC')


class PublicAlbumsView(DetailView):
    """Create instance of PublicAlbumsView object."""

    model = User
    context_object_name = 'public_albums'
    template_name = 'imager_images/public_albums.html'

    def get_object(self):
        return self.request.user.album_set.filter(published='PUBLIC')


class LogoutView(View):
    """Create instance of LogoutView object."""

    def get(self, request):
        return auth_views.logout(request)


class UpdatePhoto(UpdateView):
    """Update an instance of the photo model."""

    model = Photo
    exclude = ['image']
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
    template_name = 'imager_images/edit_photo.html'
    fields = ('title', 'description', 'published')
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateView, self).form_valid(form)


class UpdateProfile(UpdateView):
    """Update a user profile object."""

    exclude = ['user']
    slug_field = 'profile_id'
    template_name = 'imager_images/edit_profile.html'
    fields = ('website', 'location', 'commission', 'camera', 'services', 'bio', 'phone', 'photo_styles')
    success_url = '/profile/'

    def get_object(self):
        return self.request.user.imagerprofile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateView, self).form_valid(form)
