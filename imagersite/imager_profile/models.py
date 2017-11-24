"""Class for profile creation."""


from django.db import models
from django.contrib.auth.models import User


"""Sample models for a camera."""
CAMERA_MODELS = [('NikonD3300', 1), ('CanonT6i', 2), ('Canon5dMarkIII', 3)]


class ImagerProfile(models.Model):
    """Profile template for a created image."""

    user = models.OneToOneField(User)
    website = models.CharField(max_length=180)
    location = models.CharField(max_length=50)
    commission = models.FloatField(max_length=20)
    camera = models.CharField(max_length=20, choices=CAMERA_MODELS, default='1')
    services = models.TextField(max_length=2000)
    bio = models.TextField(max_length=2000)
    phone = models.CharField(max_length=14)
    photo_styles = models.TextField(max_length=400)

    @property
    def active(self):
        """Gets all active users."""
        return User.objects.all().filter(is_active=True)

    @property
    def is_active(self):
        """Gets activity setting for a given user."""
        return self.user.is_active

    def __repr__(self):
        """Return a printable version of a user."""
        return self.user.username
