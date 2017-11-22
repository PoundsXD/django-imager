from django.test import TestCase
from imager_profile.models import ImagerProfile
import factory
from django.contrib.auth.models import User
# Create your tests here.


class Userfactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class Imagersite_Tests(TestCase):
    """."""

    def test_that_imager_profile_creates_profile(self):
        """."""
        bob = User(username='fun', password='stuff')
        profile = ImagerProfile(user=bob, website='google.com', location='seattle', commission=50.00, camera='Nikon', services='I do stuff', bio='I am a person', phone='2062427983', photo_styles='all the styles')
        self.assertEquals(profile.location, 'seattle') 
