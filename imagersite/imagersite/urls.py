"""imagersite URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from imager_profile import views
from django.conf import settings
from django.conf.urls.static import static
from imager_images.views import PhotoForm, AlbumForm, LibraryView, SinglePhotoView, SingleAlbumView, LogoutView, OneProfileView, PublicPhotosView, PublicAlbumsView, UpdatePhoto, UpdateAlbum, UpdateProfile
from imager_profile.views import HomeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='homepage'),
    url(r'^profile/(?P<username>[\w\_\-]+)',  OneProfileView.as_view(), name='profile'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^profile/edit$', UpdateProfile.as_view(), name='edit-profile'),
    url(r'^images/album/(?P<pk>\w)/edit', UpdateAlbum.as_view(), name='edit-album'),
    url(r'^images/photo/(?P<pk>\w)/edit', UpdatePhoto.as_view(), name='edit-photo'),
    url(r'^images/photos/add/', PhotoForm.as_view(), name='add-photo'),
    url(r'^images/albums/add/', AlbumForm.as_view(), name='add-album'),
    url(r'^images/library/$', LibraryView.as_view(), name='library'),
    url(r'^images/photos/(?P<pk>\d+)/$', SinglePhotoView.as_view(), name='single-photo'),
    url(r'^images/albums/(?P<pk>\d+)/$', SingleAlbumView.as_view(), name='single-album'),
    url(r'^images/photos/', PublicPhotosView.as_view(), name='public-photos'),
    url(r'^images/albums/', PublicAlbumsView.as_view(), name='public-albums'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
