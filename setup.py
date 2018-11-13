import io
import os
import re

from setuptools import (setup, find_packages)

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

setup(
    name="django_lti_auth",
    version="1.0.0",
    url="https://github.com/rohitjose/django-lti-auth.git",
    license='MIT',

    author="Rohit Jose",
    author_email="rohitjose@gmail.com",

    description="Django LTI Authentication Made Easy. Easily integrate with your LTI provider for django projects",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),
    install_requires=['PyLTI==0.5.1'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
