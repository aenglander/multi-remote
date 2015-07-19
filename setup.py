from os import path
from sys import platform

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='multi-remote',
    version='0.0.1',
    author='Adam Englander',
    author_email='adam@launchkey.com',
    url='https://launchkey.com',
    summary='Multi-User Remote Control Experiment',
    license='MIT',
    description='An experiment allowing mulitple users to know and modify the state of a device',
    install_requires=['autobahn', 'twisted', 'pyOpenSSL', 'service-identity'],
    data_files=[]
)
