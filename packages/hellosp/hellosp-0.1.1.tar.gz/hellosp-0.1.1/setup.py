from setuptools import setup, find_packages
setup(
name='hellosp',
version='0.1.1',
author='Shanmuga Priya',
author_email='shanmugapriya.rs@embedur.com',
description='This is a simple package that provides sum of 2 numbers',
long_description=open("README.txt").read(),
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)