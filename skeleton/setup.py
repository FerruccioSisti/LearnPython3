#Script used to install the project later if wanted
try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    "description": "My Project",
    "author": "Ferruccio Sisti",
    "url": "N/A",
    "download_url": "N/A",
    "author_email": "ferrucciosisti@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["MAIN"],
    "scripts": [],
    "name": "projectName"
}

setup(**config)
