"""Test functionality of the imager profile module."""

from imager_images.models import Album, Photo
from django.contrib.auth.models import User
from django.test import TestCase
import datetime
from django.test import Client
from django.urls import reverse_lazy


def new_photo(username, password):
    """Custom function to create ImagerProfile with given user."""

    user = User(username=username, password=password)
    user.save()

    photo = Photo(user=user,
                  title='Dank Meme',
                  image='Puppy',
                  description='Dank ass meme about puppies')
    photo.save()
    return photo


def new_album(username, password):
    """Custom function to create ImagerProfile with given user."""

    user = User(username=username, password=password)
    user.save()

    photo = Photo(user=user,
                  title='Dank Meme',
                  image='Puppy',
                  description='Dank ass meme about puppies')
    photo.save()

    album = Album(user=user,
                  title='Dank Memes',
                  description='Public Dank Memes',
                  cover=photo)
    album.save()
    return album


class ImagerImagesTests(TestCase):
    """Test suite for testing various pieces of the imager_images app."""

    def setUp(self):
        """Defines self.client to test views."""
        self.client = Client()

    def test_photo_initialzes_with_given_values_for_attributes(self):
        """Test that an instance of a Photo model object is initialized with
        given values."""

        photo = new_photo('BobbyG', 'Bobbybethebest')
        self.assertEquals(photo.title, 'Dank Meme')
        self.assertEquals(photo.description, 'Dank ass meme about puppies')
        self.assertEquals(photo.image, 'Puppy')
        self.assertEquals(photo.user.username, 'BobbyG')
        self.assertEquals(photo.user.password, 'Bobbybethebest')

    def test_photo_initialzes_with_default_values_for_attributes(self):
        """Test that an instance of a Photo model object is initialized with
        default values."""

        photo = new_photo('ching', 'chang')
        self.assertTrue(photo.date_published, isinstance(photo.date_published, datetime.datetime))
        self.assertIn('2017', str(photo.date_published))
        self.assertTrue(photo.date_modified, isinstance(photo.date_modified, datetime.datetime))
        self.assertIn('2017', str(photo.date_modified))
        self.assertTrue(photo.date_uploaded, isinstance(photo.date_uploaded, datetime.datetime))
        self.assertIn('2017', str(photo.date_uploaded))

    def test_album_initialzes_with_given_values_for_attributes(self):
        """Test that an instance of a Album model object is initialized with
        given values."""

        album = new_album('JosephJ', 'JJdontplayplay')
        self.assertEquals(album.title, 'Dank Memes')
        self.assertEquals(album.description, 'Public Dank Memes')
        self.assertEquals(album.cover.image, 'Puppy')
        self.assertEquals(album.user.username, 'JosephJ')
        self.assertEquals(album.user.password, 'JJdontplayplay')

    def test_album_initialzes_with_default_values_for_attributes(self):
        """Test that an instance of a Album model object is initialized with
        default values."""

        album = new_album('werd', 'pass')
        self.assertTrue(album.date_published, isinstance(album.date_published, datetime.datetime))
        self.assertIn('2017', str(album.date_published))
        self.assertTrue(album.date_modified, isinstance(album.date_modified, datetime.datetime))
        self.assertIn('2017', str(album.date_modified))
        self.assertTrue(album.date_created, isinstance(album.date_created, datetime.datetime))
        self.assertIn('2017', str(album.date_created))

    def test_login_post_with_user_redirects_to_profile(self):
        """Function that tests a post request to the login route given correct
        active user credentials redirects the user to the home page."""

        active_user = User(username='Carson', password='fishfilet')
        active_user.save()

        response = self.client.post(reverse_lazy('login'),
                                    {
                                    'username': 'Carson',
                                    'password': 'fishfilet'
                                    }, follow=True)

        self.assertTemplateUsed(response, 'imager_profile/base.html')

    def test_login_page_response_is_200_with_expected_page(self):
        """Function that tests a post request to the login route given correct
        active user credentials redirects the user to the home page."""

        response = self.client.get(reverse_lazy('login'))
        username_input = '<input type="text" name="username" value="" placeholder="Username">'
        password_input = '<input type="password" name="password" value="" placeholder="Password">'

        self.assertTrue(response.status_code, "200")
        self.assertInHTML(username_input, response.rendered_content)
        self.assertInHTML(password_input, response.rendered_content)
        self.assertTrue(response.template_name, ['imager_profile/login.html'])

    def test_home_page_has_user_image_in_post_response_if_user_logged_in(self):
        """Function that tests a post request to the login route given correct
        active user credentials redirects the user to the home page."""

        response = self.client.get(reverse_lazy('homepage'))
        image = '<img src="/static/imager_profile/pretty.jpg" alt="Found on Google" height="500px"/>'

        self.assertTrue(response.status_code, "200")
        self.assertInHTML(image, str(response.content))
        self.assertTrue(response.templates[0], 'imager_profile/home.html')
