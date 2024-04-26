from setuptools import setup, find_packages
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"

with open("README.md", "r") as f:
    description = f.read()

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
setup(
    name = "StatViz",
    version = '0.0.2',
    author = "Namitha Kolu and Ashok Kumar S",
    packages = find_packages(),
    install_requires = get_requirements_list(),
    long_description=description,
    long_description_content_type="text/markdown",
)