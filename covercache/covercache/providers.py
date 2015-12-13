from django.conf import settings


def get_preferred_url(isbn):
    """
    Get URL for ISBN from preferred provider. This assumes the ISBN has been normalized.

    Right now we're only supporting Syndetics, so that's hardcoded in here.
    Later we will use settings to test for preferred providers and return
    accordingly.
    """
    url = 'http://www.syndetics.com/index.aspx?isbn={isbn}/lc.jpg&client={client_code}&type=rn12'.format(
        isbn=isbn,
        client_code=settings.COVERCACHE_AUTH['SYNDETICS']['CLIENT_CODE'])
    return url
