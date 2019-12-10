# setup.py

from setuptools import setup
from setuptools import find_packages

setup(
    name='keydifferentiator',
    url='https://github.com/Key-Differentiators/cs207-FinalProject',
    author='Kate Grosch, Spencer Penn, Mingyue Wei',
    packages=['keydifferentiator'],
    install_requires=['numpy', 'regex'],
    version='1.1',
    license='MIT',
    description='Automatic differentiation tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/x-rst'
)