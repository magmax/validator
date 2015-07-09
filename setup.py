# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [
        ('pytest-args=', 'a', "Arguments to pass to py.test"),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args or ['--cov-report=term-missing'])
        sys.exit(errno)


setup(
    name='validator',
    version='0.0.0.0.0.0.1',
    description='Document format validator, created just as a YAPSY usage example.',
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 5 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
    ],
    keywords='validator json yaml',
    author='Miguel Ángel García',
    author_email='miguelangel.garcia@gmail.com',
    url='https://github.com/magmax/validator',
    license='Affero',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
    install_requires=[
        'Yapsy >= 1.11.223',
    ],
    extras_require={
        'yaml': ['PyYAML >= 3.11'],
    },
)
