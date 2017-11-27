"""Class for profile creation."""


from django.db import models
from django.contrib.auth.models import User


class ImagerProfile(models.Model):
    """Profile template for a created image."""

    NIKOND3300 = 'NKD3300'
    CANONT6I = 'CNT6I'
    CANON5DMARKIII = 'CNMKD5III'
    SONYALPHAA99II = 'SNYA99II'

    CAMERA_MODELS = (
                    (NIKOND3300, 'NikonD3300'),
                    (CANONT6I, 'CanonT6i'),
                    (CANON5DMARKIII, 'Canon5dMarkIII'),
                    (SONYALPHAA99II, 'SonyAlphaA99II')
                    )

    ULTIMATE = 'ULT'
    MEGA = 'MEGA'
    BASIC = 'BSC'

    SERVICES = (
               (ULTIMATE, '20 photos, provided lighting equipment, additional photo editing post-production.'),
               (MEGA, '15 photos, provided lighting equipment, 5 free prints of your choice.'),
               (BASIC, '10 photos, 3 free prints of your choice.')
               )

    SEVENTIES = '70s'
    NOIR = 'NOIR'
    BOKEH = 'BOKEH'
    STUDIO = 'STUDIO'
    STANDARD = 'STD'

    STYLES = (
             (SEVENTIES, 'Classic retro style with filters to match.'),
             (NOIR, 'Bold black and white photos.'),
             (BOKEH, 'Blurry background with subject in focus.'),
             (STUDIO, 'Profile shots with bright lighting and white backdrop.'),
             (STANDARD, 'Regular shots with no filters.')
             )

    user = models.OneToOneField(User)
    website = models.CharField(max_length=180)
    location = models.CharField(max_length=50)
    commission = models.FloatField(max_length=20)
    camera = models.CharField(max_length=20, choices=CAMERA_MODELS, default=CANONT6I)
    services = models.TextField(max_length=2000, choices=SERVICES, default=MEGA)
    bio = models.TextField(max_length=2000)
    phone = models.CharField(max_length=14)
    photo_styles = models.TextField(max_length=400, choices=STYLES, default=STANDARD)

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


class Album(models.Model):
    """Create container for photos to be grouped in under a user."""

    user = models.OneToOneField(User)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=2000)
    date_published = DateTimeField()
    date_uploaded = DateTimeField(auto_now_add=True)
    daet_modified = DateTimeField(auto_now_add=True)