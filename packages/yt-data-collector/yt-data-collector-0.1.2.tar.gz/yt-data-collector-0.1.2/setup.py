from setuptools import setup, find_packages

setup(
    name='yt-data-collector',
    version='0.1.2',
    author='thesayonaraman',
    author_email='thesayonaraman@gmail.com',
    description='Project Name is a Python library for accessing and retrieving data from YouTube. It provides functions to fetch videos, channels, playlists, and search results from YouTube, enabling developers to integrate YouTube data into their applications easily.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sayonaraman',
    packages=find_packages(),
    install_requires=[
        'requests',
        'typing-extensions'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)





