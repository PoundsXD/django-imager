"""Views."""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView


class HomeView(ListView):
    """Class based view that serves the home page."""
    model = User
    context_object_name = 'user'
    template_name = 'imager_profile/home.html'

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


def profile_view(request):
    """View for user profile."""
    from django.shortcuts import redirect

    if request.user.is_authenticated():
        private_album_count = request.user.album_set.filter(published='PRIVATE')
        private_photo_count = request.user.photo_set.filter(published='PRIVATE')
        context = {'private_photos': private_photo_count,
                   'private_albums': private_album_count,
                   'profile': request.user.profile}
        return render(request, 'imager_profile/profile.html', context=context)
    else:
        return redirect('login')
