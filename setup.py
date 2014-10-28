#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from os.path import abspath, dirname, join
from setuptools import setup

version = "1.0.1"

setup(
    name="django-twilio-sms-2",
    version=version,
    description="Twilio integration for SMS-based Django apps",
    license="MIT",

    author="Saurabh Kumar",
    author_email="me@saurabh-kumar.com",

    url="https://github.com/theskumar/django-twilio-sms-2",
    download_url="https://github.com/theskumar/django-twilio-sms-2/zipball/master",

    long_description=open("README.rst").read(),

    package_dir={"django_twilio_sms": "src"},
    packages=["django_twilio_sms"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=[
        "django>=1.7",
        "djangorestframework>=2.4.3",
        "twilio>=3.6.8",
    ]
)
