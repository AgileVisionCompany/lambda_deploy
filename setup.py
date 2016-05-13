"""AWS Lambda functions deployment tool
See:
https://github.com/AgileVisionCompany/lambda_deploy
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lambda_deploy',

    version='1.0.0',

    description='AWS Lambda functions deployment tool',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/AgileVisionCompany/lambda_deploy',

    # Author details
    author='AgileVision sp. z o.o.',
    author_email='contact@agilevision.pl',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],


    keywords='aws lambda deployment',

    packages=find_packages(exclude=['lambda_deploy', 'tests']),

    install_requires=['boto3'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={
    },

    data_files=[],

    entry_points={
        'console_scripts': [
            'lambda_deploy=lambda_deploy:main',
        ],
    },
)
