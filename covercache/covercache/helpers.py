"""
This file is for utilities that are used throughout the covercache app and
therefore do not naturally belong in any of the standard Django files
(urls.py, views.py, etc.)
"""

import re

# Copied from https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9780596802837/ch04s13.html
ISBN_VALIDATOR = re.compile(r'^(?:ISBN(?:-1[03])?:? )?(?=[-0-9 ]{17}$|[-0-9X ]{13}$|[0-9X]{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?(?:[0-9]+[- ]?){2}[0-9X]')


def isbn_normalize(isbn):
    """
    We could distinguish between ISBNs with and without hyphens/spaces in
    our database, but why? There's no need to store multiple copies of images
    in our database, and to do the work of resizing them multiple times, to
    cover nonsemantic differences in user input of ISBNs.

    We will not convert ISBN-10s to ISBN-13s, because image providers have
    not necessarily done so - we may need to use the ISBN-10 to access content.
    """
    assert ( isinstance(isbn, str) or isinstance(isbn, unicode) )
    isbn = isbn.replace('-', '').replace(' ', '')
    return isbn


def is_isbn_valid(isbn):
    if re.match(ISBN_VALIDATOR, isbn):
        return True
    else:
        return False
