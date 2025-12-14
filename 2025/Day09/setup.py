from setuptools import setup, find_packages
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "floodfill.floodfill",
        ["floodfill/floodfill.pyx"],
    ),
]

setup(
    ext_modules=ext_modules,
    packages=find_packages(),
)
