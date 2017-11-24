"""Test functionality of the imager profile module."""

from django.test import TestCase
from imager_profile.models import ImagerProfile
import factory
from django.contrib.auth.models import User


class Userfactory(factory.django.DjangoModelFactory):
    """Create classes for testing user."""

    class Meta:
        """Create a class for testing user."""

        model = User


class ImagersiteTests(TestCase):
    """Test suite for testing profiles."""

    def test_that_imager_profile_creates_profile(self):
        """Test create new user."""
        bob = User(username='fun', password='stuff')
        bob.save()
        profile = ImagerProfile(user=bob, website='google.com', location='seattle', commission=50.00, camera='Nikon', services='I do stuff', bio='I am a person', phone='2062427983', photo_styles='all the styles')
        self.assertEquals(profile.location, 'seattle')
        self.assertEquals(profile.commission, 50.00)
        self.assertEquals(profile.camera, 'Nikon')
        self.assertEquals(profile.services, 'I do stuff')
        self.assertEquals(profile.bio, 'I am a person')
        self.assertEquals(profile.phone, '2062427983')
        self.assertEquals(profile.photo_styles, 'all the styles')
        self.assertEquals(profile.is_active, True)
        print(type(bob))
        print('--------')
        print(type(profile.active))
        self.assertEqual(profile.active.values()[0]['username'], 'fun')

# '<QuerySet [<User: fun>]>'