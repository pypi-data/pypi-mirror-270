# coding: utf-8

from setuptools import setup, find_packages
from distutils.util import convert_path

# https://setuptools.pypa.io/en/latest/userguide/quickstart.html

main_ns = {}
ver_path = convert_path("konciliation/__version__.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name="konciliation_GDV_target_task",
    version=main_ns["__version__"],
    install_requires=[
        "tqdm",
        "pyqt6",
        "matplotlib",
    ],
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
        include=['konciliation'],  # ['*'] by default
    ),
    entry_points={
        "console_scripts": [
                "konciliation = konciliation.main:main",
            ]
    },
    include_package_data=False,
)
