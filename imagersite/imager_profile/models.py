from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CAMERA_MODELS = [('NikonD3300', 1), ('CanonT6i', 2), ('Canon5dMarkIII', 3)]


class ImagerProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.CharField(max_length=180)
    location = models.CharField(max_length=50)
    commission = models.FloatField(max_length=20)
    camera = models.CharField(max_length=20, choices=CAMERA_MODELS, default='1')
    services = models.TextField(max_length=2000)
    bio = models.TextField(max_length=2000)
    phone = models.CharField(max_length=14)
    photo_styles = models.TextField(max_length=400)
    active = User.objects.all(User.is_active)
    is_active = User.objects.get(User.is_active)

    def __repr__(self):
        return 'User: {}.format(self)'
