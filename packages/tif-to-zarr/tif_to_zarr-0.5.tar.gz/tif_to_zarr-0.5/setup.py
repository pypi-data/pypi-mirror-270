from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'),
          encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tif_to_zarr',
    version=0.5,
    url='https://github.com/yuriyzubov/tif-to-zarr.git',
    author='Yurii Zubov',
    description='Simple package to convert small tif files to zarr format.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'imagecodecs',
        'click',
        'zarr',
        'dask', 
        'tifffile',
        ],
)