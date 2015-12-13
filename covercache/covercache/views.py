import re

from django.conf import settings
from django.http import Http404
from django.views.generic.base import View

from sorl.thumbnail import get_thumbnail

from .helpers import ISBN_VALIDATOR
from .models import IsbnObject

class ImageGetView(View):

    def validate_isbn(self, isbn):
        if not re.match(ISBN_VALIDATOR, isbn):
            raise Http404

    def get(self, request, *args, **kwargs):
        # Make sure the isbn url parameter is a valid ISBN.
        isbn = self.kwargs['isbn']
        self.validate_isbn(isbn)

        # If we already have an image for that ISBN on file, grab it.
        # Otherwise, fetch it from the first preferred source we can.
        try:
            isbn_object = IsbnObject.objects.get(isbn=isbn)
            imagefile = isbn_object.image
        except IsbnObject.DoesNotExist:
            raise Http404

        # later: add querystring parsing to determine preferred size

        get_thumbnail(imagefile, settings.THUMBNAIL_DEFAULT_SIZE)

