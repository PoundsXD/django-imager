"""Class for profile creation."""


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField


class ImagerProfile(models.Model):
    """Profile template for a created image."""

    CAMERA_MODELS = (
                    ('NikonD3300', 'NikonD3300'),
                    ('CanonT6i', 'CanonT6i'),
                    ('Canon5dMarkIII', 'Canon5dMarkIII'),
                    ('SonyAlphaA99II', 'SonyAlphaA99II')
                    )

    SERVICES = (
               ('Ultimate-Service Pack', '20 photos, provided lighting equipment, additional photo editing post-production.'),
               ('Mega-Service Pack', '15 photos, provided lighting equipment, 5 free prints of your choice.'),
               ('Basic-Service Pack', '10 photos, 3 free prints of your choice.')
               )

    STYLES = (
             ('70\'s', 'Classic retro style with filters to match.'),
             ('Noir', 'Bold black and white photos.'),
             ('Bokeh', 'Blurry background with subject in focus.'),
             ('Studio', 'Profile shots with bright lighting and white backdrop.'),
             ('Standard', 'Regular shots with no filters.')
             )

    objects = models.Manager()
    user = models.OneToOneField(User)
    website = models.CharField(max_length=180)
    location = models.CharField(max_length=50)
    commission = models.FloatField(max_length=20, blank=True, null=True)
    camera = MultiSelectField(max_length=20, choices=CAMERA_MODELS, default='CanonT6i')
    services = MultiSelectField(max_length=2000, choices=SERVICES, default='Mega-Service Pack')
    bio = models.TextField(max_length=2000)
    phone = models.CharField(max_length=14)
    photo_styles = MultiSelectField(max_length=400, choices=STYLES, default='Standard')

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    import pdb; pdb.set_trace()
    if created:
        Profile.objects.create(user=instance)
        ImagerProfile.objects.create(user=instance)
        instance.profile.save()


@receiver(post_save, sender=ImagerProfile)
def update_imager_profile(sender, instance, created, **kwargs):
    Profile.objects.create(imagerprofile=instance)
    ImagerProfile.objects.create(imagerprofile=instance)
    instance.profile.save()
