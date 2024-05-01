from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='pypanasonic',
    version='0.0.4',
    py_modules=['pypanasonic'],  # Required
    python_requires='>=3.8',
)