from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'This is a python Exclusive Encryption and hashing algorithm.'
LONG_DESCRIPTION = 'This is a an Encryption and Hashing algorithm that is designed to help facilitate the encryption of information.'

# Setting up
setup(
    name="XEHA",
    version=VERSION,
    author="Netwrk Shield(Ndep Ever Gospel)",
    author_email="<netwrkshield@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["rsa"],
    keywords=['python', 'encryption', 'cryptography', 'cipher'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)