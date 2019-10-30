# setup.py

from setuptools import setup, find_packages

setup(
    name='KeyDifferentiator',
    url='https://github.com/Key-Differentiators/cs207-FinalProject',
    author='Kate Grosch, Spencer Penn, Mingyue Wei',
    packages=['AD'],
    install_requires=['numpy'],
    version='0.1',
    license='MIT',
    description='Automatic differentiation tool',
    long_description=open('README.txt').read(),
)