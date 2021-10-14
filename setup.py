from setuptools import setup

setup(name = 'django-mailman',
    version = '0.4.1',
    packages = ['django_mailman',],
    platforms = ['any'],
    license = 'GNU LGPL v2.1',
    author = "Bernd Schlapsi",
    author_email = 'albert@albertoconnor.ca',
    description = 'Interface to Mailman Web-API',
    long_description = open('README.rst').read(),
    url = 'https://github.com/JuanCerquera/django-mailman',
    download_url = 'https://github.com/JuanCerquera/django-mailman/archive/refs/tags/0.4eso1.tar.gz'
)
