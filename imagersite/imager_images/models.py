"""."""

from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    """Photo template for a photo."""

    PUBLISHED = (
                ('PRIVATE', 'This photo is private'),
                ('SHARED', 'This photo is shared'),
                ('PUBLIC', 'This photo is public')
            )

    objects = models.Manager()
    title = models.CharField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/%Y-%m-%d')
    description = models.CharField(max_length=180)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now=True)
    published = models.CharField(max_length=20, choices=PUBLISHED, default='PRIVATE')

    @property
    def active(self):
        """Get all active users."""
        return User.objects.all().filter(is_active=True)

    @property
    def is_active(self):
        """Get activity setting for a given user."""
        return self.user.is_active

    def __repr__(self):
        """Return a printable version of a user."""
        return self.user.username


class Album(models.Model):
    """Create container for photos to be grouped in under a user."""

    PUBLISHED = (
                ('PRIVATE', 'This photo is private'),
                ('SHARED', 'This photo is shared'),
                ('PUBLIC', 'This photo is public')
            )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    photos = models.ManyToManyField(Photo, blank=True, default='', related_name='albums')
    cover = models.ForeignKey(Photo, blank=True, default='', related_name='+')
    published = models.CharField(max_length=200, choices=PUBLISHED, default='PRIVATE')
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=2000)
    date_published = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
