# -*- coding: UTF-8 -*-
from distutils.command.install import INSTALL_SCHEMES
from distutils.core import setup
from setuptools import find_packages
import re
import time
import os

_version = "0.%s.dev" % int(time.time())
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
    
    
    
# find any static content such as HTML files or CSS
_INCLUDE = re.compile("^.*\.html$") 
_root_package='adinv'
_data_files = []

for dirpath, dirnames, filenames in os.walk(_root_package):
    # ignore directories starting with a ".", eg .hg or .env
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if any([_INCLUDE.match(filename) for filename in filenames]):
        _data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])
        
# make sure that data files go into the right place
# see http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values(): 
    scheme['data'] = scheme['purelib']
    
    
    
# common dependencies
_install_requires = [
            'django>=1.3',
            'Pillow', # TODO: make this an optional dependency
            'django-gubbins<1',
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
       data_files=_data_files,

)
