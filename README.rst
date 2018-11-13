django_lti_auth
===============

.. image:: https://img.shields.io/pypi/v/django_lti_auth.svg
    :target: https://pypi.python.org/pypi/django_lti_auth
    :alt: Latest PyPI version

Django LTI Authentication Made Easy. Easily integrate with your LTI provider for Django projects. 

Usage
-----
1. Set up the app as an LTI tool on Moodle. You need to specify the following:

   a. Secure Tool URL:

    .. image:: secure_tool_url.png
        :width: 200px
        :align: center
        :height: 100px
        :alt: Secure Tool URL

   b. Consumer key and Shared secret:

    .. image:: consumer_key.png
        :width: 200px
        :align: center
        :height: 100px
        :alt: Consumer Key and Secret

2. Import the views module in your root **urls.py**

        .. code-block:: python

         # this is main url for the project
         from django.conf.urls import url, include
        
         urlpatterns += [
                url(r'^lti/', include('django_lti_auth.urls')),
                ...
         ]

3. In settings.py, add the LTI related configuration.

        .. code-block:: python

         PYLTI_CONFIG = {
                 "consumers": {
                     "<djangoConsumerKey>": {
                         "secret": "<djangoSecret>"
                     }
                 },
                 "method_hooks":{
                     "valid_lti_request":"<Specify method to call after validation of a valid LTI payload>",
                     "invalid_lti_request":"<Specify method to call after validation of an invalid LTI payload>"
                 },
                 "next_url":"<Default home page>"
             }

4. You also need to add the following settings into your settings.py file.

        .. code-block:: python
 
         X_FRAME_OPTIONS = 'ALLOW-FROM https://moodle.telt.unsw.edu.au/'
         SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
         SECURE_SSL_REDIRECT = False
         SESSION_COOKIE_SECURE = True
         CSRF_COOKIE_SECURE = True

5. Add 'django_lti_auth' to INSTALLED_APPS

        .. code-block:: python
 
         INSTALLED_APPS = [
             '...',
             'django_lti_auth',
         ]


Installation
------------

To install the package run the following command:

    .. code-block:: python

     pip install django_lti_auth


Requirements
^^^^^^^^^^^^

Licence
-------
MIT license

Authors
-------

`django_lti_auth` was written by `Rohit Jose <rohitjose@gmail.com>`_.
