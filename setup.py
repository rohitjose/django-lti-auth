from setuptools import (setup, find_packages)

setup(
    name='django_lti_auth',

    version='1.0.0',

    description='Django LTI Authentication Made Easy. Easily integrate with the LTI provider for django projects',
    long_description='Django LTI Authentication Made Easy. Easily integrate with the LTI provider for django projects',

    url='',

    author='Rohit Jose',
    author_email='rohitjose@gmail.com',

    license='Apache 2.0',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Framework :: Django :: 2.0.3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Django SAML2 Authentication Made Easy, integrate with SAML2 SSO such as Okta easily',

    packages=find_packages(),

    install_requires=['PyLTI==0.5.1'],
    include_package_data=True,
)