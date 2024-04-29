from setuptools import setup, find_packages
import pandas
VERSION = '0.0.1'
DESCRIPTION = 'DSSAT input outp fiels package'
LONG_DESCRIPTION = 'Package to create and interpret DSSAT files'

# Setting up
setup(
    name="Way2DSSAT",
    version=VERSION,
    author="Manavjot Singh",
    author_email="<manavjotsingh97@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas'],
    keywords=['python','DSSAT', 'Input', 'gSSURGO'],

)