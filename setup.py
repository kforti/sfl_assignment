#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

install_requires = open("requirements.txt").read().strip().split("\n")
requirements = ['Click',
                'python_dotenv',
                ] + install_requires

test_requires = open("test-requirements.txt").read().strip().split("\n")
test_requirements = ['pytest>=3',
                     ] + test_requires

setup(
    author="Kevin Fortier",
    author_email='',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="",
    entry_points={
        'console_scripts': [
            'sfl_assignment=sfl_assignment.cli:run_command',
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    keywords='python_package',
    name='python_package',
    packages=find_packages(include=['sfl_assignment', 'sfl_assignment.*']),
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
