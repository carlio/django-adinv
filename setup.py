# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages
import time


_version = "0.%s.dev" % int(time.time())
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
    
# common dependencies
_install_requires = [
            'django',
       ]

setup( name='django-adinv',
       url='https://github.com/carlio/django-adinv',
       author='Carl Crowder',
       author_email='django-adinv@jqx.be',
       version=_version,
       packages=_packages,
       install_requires=_install_requires,
       scripts=[
           # 'scripts/manage',
       ],

)
