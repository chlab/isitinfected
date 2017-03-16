"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from isitinfected import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=isitinfected', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'isitinfected',
    version = __version__,
    description = 'Machine learning tool to determine if beers are infected',
    long_description = long_description,
    url = 'https://github.com/chlab/isitinfected',
    author = 'Christof Leuenberger',
    author_email = 'mail@chlab.ch',
    license = 'BEERWARE',
    classifiers = [
        'Intended Audience :: Brewers',
        'Topic :: Utilities',
        'License :: Beerware'
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'isitinfected=isitinfected.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)