from django.forms import BaseForm
from django import forms
from imager_profile.models import ImagerProfile


class ImagerProfileUpdateForm(BaseForm):
    """Class for email registration form."""
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Please provide a valid email address.')

    class Meta:
        model = ImagerProfile
        fields = ('website', 'location', 'commission', 'camera', 'services', 'bio', 'phone', 'photo_styles', 'first_name', 'last_name', 'email')
