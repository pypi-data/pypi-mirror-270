# setup.py

from setuptools import setup, find_packages

VERSION = '0.0.15'
DESCRIPTION = 'A Caribbean watershed shapefile downloader package.'
LONG_DESCRIPTION = 'Python package for downloading country-specific Caribbean watershed data.'

setup(
    name='IslandSheds',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'geopandas',
        'requests',
        'json'
    ],
    author='Kent Thomas',  # Placeholder for author name
    author_email='kthomas.wsrn@gmail.com',  # Placeholder for author email
    description=DESCRIPTION,
    long_description_content_type= "text/markdown",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/kgdthomas/IslandSheds',  # Placeholder for GitHub repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
