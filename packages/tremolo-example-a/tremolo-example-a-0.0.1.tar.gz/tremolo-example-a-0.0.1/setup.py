#!/usr/bin/env python3

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='tremolo-example-a',
    version='0.0.1',
    license='MIT',
    author='nggit',
    author_email='contact@anggit.com',
    description=(
        'tremolo-example-a is basically an extension of tremolo-example.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://pypistats.org/packages/tremolo-example-a',
    packages=['tremolo_example_a'],
    install_requires=['tremolo_session'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
