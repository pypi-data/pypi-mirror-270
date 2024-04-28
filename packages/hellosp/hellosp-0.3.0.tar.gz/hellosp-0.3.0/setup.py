from setuptools import setup, find_packages
setup(
name='hellosp',
version='0.3.0',
author='Shanmuga Priya',
author_email='shanmugapriya.rs@embedur.com',
description='This is a simple cli to calculate the sum of 2 numbers',
long_description=open("README.md").read(),
packages=find_packages(),
entry_points={
        "console_scripts": [
            "hellosp = hellosp.cli:main"
        ]
    },
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)