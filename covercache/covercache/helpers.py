"""
This file is for utilities that are used throughout the covercache app and
therefore do not naturally belong in any of the standard Django files
(urls.py, views.py, etc.)
"""

import re

# Copied from the Regular Expressions Cookbook at
# https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9781449327453/ch04s13.html,
# because ain't nobody got time to write their own ISBN regex.
ISBN_VALIDATOR = re.compile(r'(?:ISBN(?:-1[03])?:? )?(?=[-0-9 ]{17}$|[-0-9X ]{13}$|[0-9X]{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?(?:[0-9]+[- ]?){2}[0-9X]$')


def isbn_normalize(isbn):
    """
    We could distinguish between ISBNs with and without hyphens/spaces in
    our database, but why? There's no need to store multiple copies of images
    in our database, and to do the work of resizing them multiple times, to
    cover nonsemantic differences in user input of ISBNs. Similarly we
    could handle ISBN 10s and 13s separately, but nope. We're going to
    normalize ISBNs before storing or interacting with IsbnObjects.
    """
    assert isinstance(isbn, str)
    isbn = isbn.replace('-', '').replace(' ', '')
    if len(isbn) == 10:
        isbn = '978' + isbn
    return isbn
