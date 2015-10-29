from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = True

    def run_tests(self):
        import pytest
        import sys
        cmdline = ' -v --doctest-modules --cov surt surt/'
        errcode = pytest.main(cmdline)
        sys.exit(errcode)


setup(name='surt',
      version='0.3b2',
      author='rajbot',
      author_email='raj@archive.org',
      classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
      ],
      description='Sort-friendly URI Reordering Transform (SURT) python package.',
      long_description=open('README.md').read(),
      url='https://github.com/rajbot/surt',
      zip_safe=True,
      install_requires=[
          'six',
          'tldextract',
      ],
      provides=[ 'surt' ],
      packages=[ 'surt' ],
      scripts=[],
      # Tests
      tests_require=[ 'pytest' ],
      test_suite='',
      cmdclass={'test': PyTest},
     )
