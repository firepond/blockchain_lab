#!/usr/bin/env python

from setuptools import setup

setup(
    name='bip32utils',
    version='0.3-4',
    author='Johnathan Corgan, Corgan Labs',
    author_email='johnathan@corganlabs.com',
    maintainer='Pavol Rusnak',
    maintainer_email='stick@gk2.sk',
    url='http://github.com/prusnak/bip32utils',
    description='Utilities for generating and using Bitcoin Hierarchical Deterministic wallets (BIP0032).',
    license='MIT',
    install_requires=['ecdsa'],
    packages=['bip32utils'],
    scripts=['bip32gen']
)
