from django.db import models

from sorl.thumbnail import ImageField


class IsbnObject(models.Model):
    """
    The bare minimum needed model: an ISBN and an image.

    The real world might be more complicated than this, but that's a problem
    for later. ISBN validation is definitely more complicated than this; also,
    later.
    """
    isbn = models.CharField(max_length=20)
    image = ImageField()
