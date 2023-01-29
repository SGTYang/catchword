from setuptools import setup, find_packages
from wordsearch.info import __package_name__, __version__

# open and read README.md file
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


setup(
    name=__package_name__,
    version=__version__,
    long_description=readme,
    packages=find_packages(),
    python_requires=">3.9",
    entry_points={"console_scripts": ["wordsearch=wordsearch.main:main"]},
)
