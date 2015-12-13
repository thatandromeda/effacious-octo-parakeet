from django.core.exceptions import ValidationError
from django.db import models

from sorl.thumbnail import ImageField

from .helpers import isbn_normalize, is_isbn_valid

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
    isbn = models.CharField(max_length=13)
    image = ImageField()

    def save(self, *args, **kwargs):
        self.isbn = isbn_normalize(self.isbn)
        if is_isbn_valid(self.isbn):
            super(IsbnObject, self).save(*args, **kwargs)
        else:
            raise ValidationError
