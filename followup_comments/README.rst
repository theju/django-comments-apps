========
INSTALL
========

* Add ``django.contrib.comments`` and ``followup_comments`` to ``INSTALLED_APPS``.
* Add the ``COMMENTS_APP`` attribute to ``settings.py`` to reference ``followup_comments``.
* Add a few additional attributes to the ``settings.py`` namely
    * ``EMAIL_HOST``: If your SMTP server is on a different machine
    * ``EMAIL_PORT``: If your port is different than a default
    * ``EMAIL_HOST_USER``: If authentication is enabled on SMTP server
    * ``EMAIL_HOST_PASSWORD``: If authentication is enabled
    * ``DEFAULT_FROM_EMAIL``: If you want to specify the from address

* Go to the admin page and add a Followup Message for the site of your choice.
