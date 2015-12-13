import re

from django.db import models

from sorl.thumbnail import ImageField

from .helpers import isbn_normalize, ISBN_VALIDATOR

class IsbnObject(models.Model):
    """
    The bare minimum needed model: an ISBN and an image.

    The real world might be more complicated than this, but that's a problem
    for later.

    The system may encounter ISBNs in many forms, but they will all be
    normalized to 13-digit integers before being saved. Similarly,
    functions interacting with IsbnObjects are responsible for normalizing
    ISBNs before checking for them.
    """
    isbn = models.IntegerField()
    image = ImageField()

    def save(self, *args, **kwargs):
        assert re.match(ISBN_VALIDATOR, self.isbn)
        self.isbn = isbn_normalize(self.isbn)
        super(IsbnObject, self).save(*args, **kwargs)
