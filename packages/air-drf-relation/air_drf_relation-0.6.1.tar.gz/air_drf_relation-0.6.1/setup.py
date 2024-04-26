from setuptools import setup, find_packages

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='air_drf_relation',
      version='0.6.1',
      description='Improved interaction with DRF relations.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords='django rest relation nested pk primary object',
      url='https://github.com/bubaley/air-drf-relation',
      author='bubaley',
      author_email='bubaley.fu@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'djangorestframework>=3.14.0',
          'django-filter',
          'django>=4.2.2',
          'dacite>=1.8.1',
          'djangorestframework-dataclasses>=1.2.0'
      ],
      include_package_data=True,
      zip_safe=False)
