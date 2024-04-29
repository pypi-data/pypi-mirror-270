# setup.py

from setuptools import setup, find_packages

VERSION = '0.0.17'
DESCRIPTION = 'A Caribbean watershed shapefile downloader package.'
LONG_DESCRIPTION = 'Python package for downloading country-specific Caribbean watershed data.'

setup(
    name='IslandSheds',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'geopandas',
        'requests',
    ],
    author='Kent Thomas',
    author_email='kthomas.wsrn@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/kgdthomas/IslandSheds',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='watershed geospatial data download Caribbean',
    license='MIT',
    include_package_data=True,
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'islandsheds=islandsheds.downloader:main',
        ],
    },
    project_urls={
        'Documentation': 'https://islandsheds.readthedocs.io/',
        'Source': 'https://github.com/kgdthomas/IslandSheds',
        'Tracker': 'https://github.com/kgdthomas/IslandSheds/issues',
    },
)