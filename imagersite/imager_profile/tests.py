"""Test functionality of the imager profile module."""

from django.test import TestCase
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User


def new_profile(username, password):
    """Custom function to create ImagerProfile with given user."""

    user = User(username=username, password=password)
    user.save()

    return ImagerProfile(user=user,
                         website='google.com',
                         location='seattle',
                         commission=50.00, camera='Nikon',
                         services='I do stuff',
                         bio='I am a person',
                         phone='2062427983',
                         photo_styles='all the styles')


class ImagersiteTests(TestCase):
    """Test suite for testing profiles."""

    def test_that_imager_profile_creates_profile_with_given_user(self):
        """Test creation of ImagerProfile creates a profile with correct
        given values, including access to User username and password."""

        profile = new_profile('Bman', 'bbybethebest')
        self.assertEquals(profile.location, 'seattle')
        self.assertEquals(profile.commission, 50.00)
        self.assertEquals(profile.camera, 'Nikon')
        self.assertEquals(profile.services, 'I do stuff')
        self.assertEquals(profile.bio, 'I am a person')
        self.assertEquals(profile.phone, '2062427983')
        self.assertEquals(profile.photo_styles, 'all the styles')
        self.assertEquals(profile.user.username, 'Bman')
        self.assertEquals(profile.user.password, 'bbybethebest')

    def test_that_imager_profile_methods_return_correct_values(self):
        """Test ImagerProfile methods return correct values."""

        profile = new_profile('BobbyG', 'Bobbybethebest')
        self.assertEquals(profile.is_active, True)
        self.assertEqual(profile.active.values()[0]['username'], 'BobbyG')
        self.assertEqual(profile.active.values()[0]['password'], 'Bobbybethebest')

    def test_imager_profile_camera_styles_services_default_values(self):
        """Test default values for camera, photo_styles, and services are
        given to new ImagerProfile if no values entered."""

        bob = User('bobdude', password='bobduderules')
        profile = ImagerProfile(user=bob, website='google.com', location='seattle', commission=100.00, bio='I am a person', phone='2062427983')
        self.assertEquals(profile.camera, 'CanonT6i')
        self.assertEquals(profile.services, 'Mega-Service Pack')
        self.assertEquals(profile.photo_styles, 'Standard')
