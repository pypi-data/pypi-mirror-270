from setuptools import setup, find_packages

setup(
    name = 'sectec',
    version = '1.2',
    description = 'Easy to use Webscraper module for python',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author = 'Ali Lodhi',
    author_email = 'alilodhibusiness@gmail.com',
    packages = ['sectec'],
    install_requires = [
        'requests == 2.31.0',
        'bs4 == 0.0.2'
    ],
)