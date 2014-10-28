django-twilio-sms-2
===================

Fork of django-twilio-sms by nigma. Maintained by Saurabh Kumar.

Twilio integration for SMS-based Django apps

.. image:: https://pypip.in/v/django-twilio-sms-2/badge.png
    :target: https://pypi.python.org/pypi/django-twilio-sms-2/
    :alt: Latest Version

.. image:: https://pypip.in/d/django-twilio-sms-2/badge.png
    :target: https://pypi.python.org/pypi/django-twilio-sms-2/
    :alt: Downloads

.. image:: https://pypip.in/license/django-twilio-sms-2/badge.png
    :target: https://pypi.python.org/pypi/django-twilio-sms-2/
    :alt: License


Quickstart
----------

1. Include ``https://github.com/theskumar/django-twilio-sms/archive/master.zip`` in your ``requirements.txt`` file.

2. Add ``django_twilio_sms`` to ``INSTALLED_APPS`` and syncdb/migrate.

3. Add the following url to your urlconf:

   .. code-block:: python

       url(r"^messaging/", include("django_twilio_sms.urls")),

   this will receive confirmation callbacks for any SMS message
   that you send using ``utils.send_sms``.

4. Create a new view and override ``IncomingSMSView.post_save(self, obj)`` method
   to receive SMS messages via callbacks from Twilio. The received ``obj``
   param will be an instance of ``IncomingSMS`` model.

5. Configure Twilio callback to send notifications to the above view's url.

6. Configure settings:

   - `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` - copy
     credentials from the Twilio panel.

   - `TWILIO_CALLBACK_USE_HTTPS` - use https or not for delivery confirmation
     callback urls.

   - `TWILIO_CALLBACK_DOMAIN` - optionally set domain name or IP of your site
     (otherwise the server name will be extracted from the request info).

   - `TWILIO_DRY_MODE` - set if you want to run in test mode.

Dependencies
------------

- django>=1.7
- djangorestframework>=2.4.3
- twilio>=3.6.8


Further Reading
---------------

- https://www.twilio.com/docs/api/rest/sending-messages

License
-------

``django-twilio-sms-2`` is released under the MIT license.

Other Resources
---------------

- GitHub repository - https://github.com/theskumar/django-twilio-sms-2
- PyPi Package site - http://pypi.python.org/pypi/django-twilio-sms-2

