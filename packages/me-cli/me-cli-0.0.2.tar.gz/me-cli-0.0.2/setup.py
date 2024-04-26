from setuptools import find_packages
from setuptools import setup

from src.me_cli import __version__

with open("requirements.txt") as req_file:
    requirements = req_file.read().splitlines()

setup(
    author="Pieter Thomas",
    author_email="dev@pieterthomas.be",
    description="CLI which allows me to do work easier and quicker.",
    entry_points={
        "me_cli": [
            "me_cli=me_cli.cli:main"
        ]
    },
    install_requires=requirements,
    license="",
    name="me-cli",
    package_dir={"": "src"},
    packages=find_packages(where="src", include=["me_cli*"]),
    version=__version__,
)
