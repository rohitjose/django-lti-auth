django_lti_auth
===============

.. image:: https://img.shields.io/pypi/pyversions/django_lti_auth.svg
    :target: https://pypi.python.org/pypi/django_lti_auth

.. image:: https://img.shields.io/pypi/v/django_lti_auth.svg
    :target: https://pypi.python.org/pypi/django_lti_auth
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/django_lti_auth.svg
    :target: https://pypi.python.org/pypi/django_lti_auth

This project aims to provide a dead simple way to integrate LTI Authentication into your Django powered app. Try it now, and get rid of the complicated configuration of LTI.

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

Explanation
------------
* valid_lti_request - The module calls the method you specify here after validating the LTI payload if the payload is valid. The method passes the LTI payload values extracted into a python dictionary as an argument to this method. You can use this payload to bind the user variables to the session. 

        .. code-block:: python

         def valid_lti_request(user_payload, request):
             ...
             request.session['userid'] = user_payload['user_id'] 
             request.session['roles'] =  user_payload['roles']
             request.session['context_id'] = user_payload['context_id']
             ...

 You can return a URL value in case you want to redirect the LTI authenticated user to a new URL after the LTI Authentication.

        .. code-block:: python

         def valid_lti_request(user_payload, request):
             ...
             url = reverse('<intented URL string>', kwargs={'context': user_payload['context_id'], 'userid':user_payload['user_id']})
             return url

         
* invalid_lti_request: This method is called after validation when the LTI payload is invalid. You can use this method to redirect the user back to the login page (or an access denied page).

Installation
------------

To install the package run the following command:

    .. code-block:: python

     pip install django_lti_auth


Requirements
^^^^^^^^^^^^
.. code-block:: python
 
  PyLTI==0.5.1

Licence
-------
MIT license

Authors
-------

`django_lti_auth` was written by `Rohit Jose <rohitjose@gmail.com>`_.
