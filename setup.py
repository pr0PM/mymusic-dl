#!/usr/bin/env python

import setuptools

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as r:
    requirements = r.read().splitlines()


setuptools.setup(
    name='mymusic_dl',
    version='0.0.1b0',
    python_requires='>=3',
    install_requires=requirements,
    author='Prateek Mishra',
    author_email='pr0pm@pm.me',
    url='https://github.com/pr0PM/mymusic-dl/',
    description='Download your music playlists using web-scraping and youtube-dl no API keys involved',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='music download youtube spotify playlist',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mymusic_dl=mymusic_dl.main:mymusic_dl',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Topic :: Internet',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Intended Audience :: End Users/Desktop',
    ],
)
