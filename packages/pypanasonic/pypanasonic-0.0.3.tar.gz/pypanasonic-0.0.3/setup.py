from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='pypanasonic',
    version='0.0.2',
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.8',
)