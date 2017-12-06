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
    title = models.CharField(max_length=180, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/%Y-%m-%d')
    description = models.CharField(max_length=180)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now=True)
    published = models.CharField(max_length=20, choices=PUBLISHED, default='PRIVATE')


class Album(models.Model):
    """Create container for photos to be grouped in under a user."""

    PUBLISHED = (
                ('PRIVATE', 'This album is private'),
                ('SHARED', 'This album is shared'),
                ('PUBLIC', 'This album is public')
            )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    photos = models.ManyToManyField(Photo, blank=True, default='', related_name='albums')
    cover = models.ForeignKey(Photo, blank=True, default='', related_name='+')
    published = models.CharField(max_length=200, choices=PUBLISHED, default='PRIVATE')
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=2000)
    date_published = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
