# -*- coding: utf-8 -*-
import os
import sys
import shlex
import subprocess
import django_emailsupport

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages  # NOQA

version = django_emailsupport.__versionstr__


# release a version, publish to GitHub and PyPI
if sys.argv[-1] == 'publish':
    command = lambda cmd: subprocess.check_call(shlex.split(cmd))
    command('git tag v' + version)
    command('git push --tags origin master:master')
    command('python setup.py sdist upload')
    sys.exit()

base_path = os.path.dirname(__file__)


def read_file(filename):
    return open(os.path.join(base_path, filename)).read()

setup(
    name='django-emailsupport',
    version=version,
    description='Simple email support over django admin',
    long_description=read_file('README.rst'),
    author='Martin Voldrich',
    author_email='rbas.cz@gmail.com',
    url='https://github.com/rosti-cz/django-emailsupport',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'Django>=1.7', 'imbox',
    ],
    zip_safe=False,
    package_data={'django_emailsupport': ['templates/admin/*', 'static/*/css/*', 'LICENSE']},
    include_package_data=True,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    )
)
