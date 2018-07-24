
from setuptools import setup, find_packages
import sys, os

setup(name='nog4now',
    version='1.0',
    description="No Glance For Now (nog4now)",
    long_description="No Glance For Now (nog4now)",
    classifiers=[],
    keywords='',
    author='Arash Morattab',
    author_email='im.4rash@gmail.com',
    url='TBA',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        nog4now = nog4now.cli.main:main
    """,
    namespace_packages=[],
    )
