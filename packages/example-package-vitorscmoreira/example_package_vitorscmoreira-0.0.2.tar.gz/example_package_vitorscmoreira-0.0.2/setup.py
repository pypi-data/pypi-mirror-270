from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

PACKAGE_NAME = 'example_package_vitorscmoreira'
VERSION = '0.0.2'
AUTHOR_EMAIL = "vitorscmoreira@hotmail.com"
AUTHOR_NAME = 'Vitor Moreira'
DESCRIPTION = 'Package description'
LONG_DESCRIPTION = 'Package long description'


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['os'],
    keywords=['python', 'rpa'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)