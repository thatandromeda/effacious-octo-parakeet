import logging
import re
import urllib2

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.http import Http404, HttpResponse
from django.views.generic.base import View

from sorl.thumbnail import get_thumbnail

from .helpers import ISBN_VALIDATOR, isbn_normalize
from .models import IsbnObject
from . import providers


logger = logging.getLogger(__name__)


class ImageGetView(View):

    http_method_names = ['get']

    def _validate_isbn(self, isbn):
        if not re.match(ISBN_VALIDATOR, isbn):
            logger.info('Attempt to access invalid isbn {isbn}'.format(isbn=isbn))
            raise Http404

    def get(self, request, *args, **kwargs):
        # Make sure the isbn url parameter is a valid ISBN.
        isbn = self.kwargs['isbn']
        self._validate_isbn(isbn)
        isbn = isbn_normalize(isbn)

        # If we already have an image for that ISBN on file, grab it.
        # Otherwise, fetch it from the first preferred source we can.
        try:
            isbn_object = IsbnObject.objects.get(isbn=isbn)
            imagefile = isbn_object.image
        except IsbnObject.DoesNotExist:
            # Right now, we're downloading the file and then returning its
            # local URL
            # Later, we should return URL of image from preferred provider and hope for the best
            # Then fetch image from provider asynchronously
            # And check to be sure it's nonempty
            # How do I handle filetype validation for the Django filefield extension??

            url = providers.get_preferred_url(isbn)

            isbn_object = IsbnObject()
            isbn_object.isbn = isbn

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(url).read())
            img_temp.flush()

            filename = '{base}.{extension}'.format(base=isbn, extension='jpg')

            isbn_object.image.save(filename, File(img_temp))
            imagefile = isbn_object.image

            # TODO make sure you delete these
            # TODO storages

        # later: add querystring parsing to determine preferred size

        thumbnail = get_thumbnail(imagefile, settings.THUMBNAIL_DEFAULT_SIZE)

        return HttpResponse(thumbnail.url)

