from imager_images.models import Photo
from django.views.generic import TemplateView

# Create your views here.


class PhotoForm(TemplateView):
        model = Photo
        exclude = []
        template_name = 'imager_profile/create_photo.html'
        fields = ('title', 'user', 'image', 'description', 'date_uploaded', 'date_modified', 'date_published', 'published')
        success_url = '/profile/'
