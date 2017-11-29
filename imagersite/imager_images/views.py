from imager_images.models import Photo
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.


class PhotoForm(CreateView):
        model = Photo
        exclude = []
        template_name = 'imager_profile/create_photo.html'
        fields = ('title', 'image', 'description', 'published')
        success_url = '/profile/'

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(CreateView, self).form_valid(form)


