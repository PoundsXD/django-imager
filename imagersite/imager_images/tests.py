"""Test functionality of the imager profile module."""

from imager_images.models import Album, Photo
from django.contrib.auth.models import User
from django.test import TestCase
import datetime
from django.test import Client
from django.urls import reverse_lazy
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile as Sup
import tempfile


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
        settings.MEDIA_ROOT = tempfile.mkdtemp()

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
        self.assertIsNone(photo.date_published)
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
        self.assertIsNone(album.date_published)
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

    def test_home_page_content_in_get_response_if_user_logged_out(self):
        """Function that tests the content in the homepage if the user is not
        logged in."""

        response = self.client.get(reverse_lazy('homepage'))
        image = '<img src="/static/imager_profile/pretty.jpg" alt="Found on Google" height="500px"/>'

        self.assertTrue(response.status_code, "200")
        self.assertInHTML(image, str(response.content))
        self.assertTrue(response.templates[0], 'imager_profile/home.html')

    def test_home_page_content_in_get_response_if_user_logged_in(self):
        """Function that tests the content in the homepage if the user is
        logged in."""

        active_user = User(username='Carsona', password='fishfileta')
        active_user.save()

        self.client.force_login(active_user)
        response = self.client.get('/')
        image = '<h2>Welcome back, Carsona.</h2>'

        self.assertTrue(response.status_code, "200")
        self.assertInHTML(image, str(response.content))
        self.assertTrue(response.templates[0], 'imager_profile/home.html')

    def test_profile_page_content_in_get_response_if_user_logged_in(self):
        """Function that tests the content in the profile page if the user is
        logged in."""

        active_user = User(username='Carsonita', password='fishfiletita')
        active_user.save()

        self.client.force_login(active_user)
        response = self.client.get('/profile/')

        pub_photos = '<h3>PUBLIC PHOTO COUNT: 0</h3>'
        priv_albums = '<h3>PRIVATE ALBUM COUNT: 0</h3>'
        priv_photos = '<h3>PRIVATE PHOTO COUNT: 0</h3>'
        pub_albums = '<h3>PUBLIC ALBUM COUNT: 0</h3>'

        self.assertTrue(response.status_code, "200")
        self.assertIn(pub_photos, str(response.content))
        self.assertIn(priv_photos, str(response.content))
        self.assertIn(pub_albums, str(response.content))
        self.assertIn(priv_albums, str(response.content))
        self.assertIn('<form method="POST">', str(response.content))

    def test_profile_page_redirects_user_if_user_logged_out(self):
        """Function that tests the user gets redirected to the login page if
        they are logged out and try to access the profile route."""

        response = self.client.get('/profile/', follow=True)

        pub_photos = '<h3>PUBLIC PHOTO COUNT: 0</h3>'
        priv_albums = '<h3>PRIVATE ALBUM COUNT: 0</h3>'
        priv_photos = '<h3>PRIVATE PHOTO COUNT: 0</h3>'
        pub_albums = '<h3>PUBLIC ALBUM COUNT: 0</h3>'

        self.assertNotIn(pub_photos, str(response.content))
        self.assertNotIn(priv_photos, str(response.content))
        self.assertNotIn(pub_albums, str(response.content))
        self.assertNotIn(priv_albums, str(response.content))

        username = '<input type="text" name="username" value="" placeholder="Username">'
        password = '<input type="password" name="password" value="" placeholder="Password">'

        self.assertIn(username, str(response.content))
        self.assertIn(password, str(response.content))

    def test_register_page_content_in_get_response_if_user_logged_out(self):
        """Function that tests the content in the register page if the user is
        not logged in."""

        response = self.client.get('/register/')

        registration_header = 'Register: Use the form below to register.'

        self.assertTrue(response.status_code, "200")
        self.assertIn(registration_header, str(response.content))
        self.assertTrue(response.templates[0], 'imager_profile/home.html')

    def test_register_valid_post_sends_email_to_backend(self):
        """Function that tests the content in the register page if the user is
        not logged in."""
        from django.core import mail

        response = self.client.post(reverse_lazy('register'), {'username': 'Cmoney',
                                                               'password1': 'moneypies',
                                                               'password2': 'moneypies',
                                                               'email': 'cmoney@money.pies'}
                                    )
        email = mail.outbox[0]

        self.assertTrue(response.status_code, "200")
        self.assertEqual(email.subject, 'Activate Your Imgine Account')
        self.assertIn('Click on the link below to confirm your registration!', email.message().get_payload())
        self.assertIn('Hello Cmoney!,', email.message().get_payload())

    def test_register_redirects_user_to_activation_page(self):
        """Function that tests the content in the register page if the user is
        not logged in."""

        response = self.client.post(reverse_lazy('register'), {'username': 'Cmoney',
                                                               'password1': 'moneypies',
                                                               'password2': 'moneypies',
                                                               'email': 'cmoney@money.pies'}
                                    , follow=True)
        activation_h1 = '<h1>Activation Sent!</h1>'

        self.assertTrue(response.status_code, "200")
        self.assertIn(activation_h1, str(response.content))

    def test_registration_link_activates_user_and_redirects_to_login(self):
        """Function that tests the content in the register page if the user is
        not logged in."""
        from django.contrib.auth.models import User
        from django.core import mail

        response = self.client.post(reverse_lazy('register'), {'username': 'Cmoney',
                                                               'password1': 'moneypies',
                                                               'password2': 'moneypies',
                                                               'email': 'cmoney@money.pies'}
                                    )
        email = mail.outbox[0]
        activation = email.body.split('\n')[7]

        response = self.client.get(activation, follow=True)
        login_page_h1 = '<h1>Welcome back! Use the form below to sign in!</h1>'

        self.assertTrue(User.objects.get(username='Cmoney').is_active)
        self.assertTrue(response.status_code, "200")
        self.assertIn(login_page_h1, str(response.content))

    def test_create_album_view_form_creates_album_in_db(self):
        """Function that tests AlbumView form successfullt creates a new Album
        model object and enters it into the database."""

        active_user = User(username='james', password='jenkins')
        active_user.save()
        photo = new_photo('CarsonGman', 'carsonisthebest')

        self.client.force_login(active_user)
        response = self.client.post(reverse_lazy('add-album'), {
                                    'photos': [photo.id],
                                    'cover': photo.id,
                                    'title': 'Dank Ass Memes',
                                    'description': 'The dankest..........',
                                    'published': 'PRIVATE'
                                    }, follow=True)
        self.assertTrue(response.status_code, "200")
        self.assertEquals(Album.objects.count(), 1)
        # self.assertTrue(album.published, 'PRIVATE')
