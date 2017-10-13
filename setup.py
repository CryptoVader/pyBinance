#!/usr/bin/env python
from setuptools import setup

setup(
    name='pybinance',
    version='0.0.1',
    packages=['binance'],
    description='This is a Python wrapper for the Binance REST API',
    url='https://github.com/CryptoVader/pyBinance',
    download_url = 'https://github.com/CryptoVader/pyBinance/archive/0.0.1.tar.gz',
    author='Guillaume Jeanne',
    license='MIT',
    author_email='',
    install_requires=['requests'],
    keywords='binance exchange bitcoin ethereum litecoin api rest',
    classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)