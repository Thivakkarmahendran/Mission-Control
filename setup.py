from pkg_resources import Version
from setuptools import setup
import METADATA

setup(
   name = METADATA.APP_NAME,
   version = METADATA.Version,
   description = METADATA.DESCRIPTION,
   author = 'Thivakkar Mahendran',
   author_email = 'mthivakkar@gmail.com',
   packages = ['mission-control'] 
)