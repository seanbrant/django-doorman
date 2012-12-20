import re
from os import path
from setuptools import setup, find_packages


def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_file = read(*file_paths)
    version_match = re.search(version_re, version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='django-doorman',
    version=find_version('doorman', '__init__.py'),
    url='https://github.com/seanbrant/django-doorman',
    author='Sean Brant',
    author_email='brant.sean@gmail.com',
    license='BSD',
    description='Flexible permission backend',
    long_description=read('README.rst'),
    packages=['doorman'],
    install_requires=[
        'django>=1.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
