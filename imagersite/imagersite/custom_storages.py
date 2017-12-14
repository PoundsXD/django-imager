"""S3 bucket paths."""

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    """Class for storage of static files in s3 bucket."""

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    """Class for storage of media in s3 bucket."""

    location = settings.MEDIAFILES_LOCATION
