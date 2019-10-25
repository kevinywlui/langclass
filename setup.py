#!/usr/bin/env python

from setuptools import setup

setup(name='langclass',
      version='1.0',
      description='Machine learning model to classify programming languages',
      author='Kevin Lui',
      author_email='kevinywlui@gmail.com',
      entry_points={'console_scripts': ['langclass = langclass.models.predict_model_cli:predict']},
     )
