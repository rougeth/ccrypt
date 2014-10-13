import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='ccrypt',
    version='0.02',
    description='Implementation of classical encryption algorithms',
    author='Marco Rougeth',
    author_email='marco@rougeth.com',
    url='https://github.com/rougeth/ccrypt',
    license='',
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
)
