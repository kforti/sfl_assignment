#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

install_requires = open("requirements.txt").read().strip().split("\n")
requirements = ['Click',
                'python_dotenv',
                ] + install_requires


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
            'run_etl_pipeline=sfl_assignment.cli:run_etl_pipeline',
            'create_database=sfl_assignment.cli:create_database',
            'remove_database=sfl_assignment.cli:remove_database',
            'show_records=sfl_assignment.cli:print_all_records',
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    keywords='sfl_assignment',
    name='sfl_assignment',
    packages=find_packages(include=['sfl_assignment', 'sfl_assignment.*']),
    zip_safe=False,
)
