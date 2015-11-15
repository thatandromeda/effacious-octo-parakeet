# effacious-octo-parakeet

To set this up on your localhost...

* Set the following environment variables:
  * `DJANGO_SECRET_KEY` (you can generate a Django secret key at http://www.miniwebtool.com/django-secret-key-generator/)
  * `DJANGO_SETTINGS_MODULE` (dotted path to your settings file, e.g. `covercache.settings.production`)
* Establish a database that matches the DATABASES setting of your settings file.
* `pip install -r requirements.txt` (you will be happiest doing this inside of a [virtualenv](https://virtualenvwrapper.readthedocs.org/))
* `python covercache/manage.py migrate` (you only need to do this the first time you set it up, or after the database schema has changed)
* `python covercache/manage.py runserver` Yay, now you have a Django app at 127.0.0.1:8000.