from setuptools import setup, find_packages

setup(
name='RP2040Home',
version='0.1.0',
author='Ellington S',
author_email='',
description='MQTT Client for RP2040 based boards which integrates into Home Assistant',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)