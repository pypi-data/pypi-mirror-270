from setuptools import setup, find_packages

setup(
  name='Flare_Helper',
  version='1.0.0',
  description='A python module used to make the authentication request more clean',
  url='https://github.com/t-a-g-o/flare',  
  author='tago',
  license='MIT',
  packages=find_packages(),
  install_requires= ['requests', 'uuid']
)