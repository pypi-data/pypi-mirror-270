# setup.py
from setuptools import setup, find_packages

setup(
    name="pieplinepy",
    version="0.2",
    packages=find_packages(),
    description="A custom pipeline library for data transformations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zakaria Morchid",
    author_email="morchid.zakariaa@gmail.com",
    keywords="pipeline data transformation",
    url="https://github.com/mzakariabigdata/pieplinepy",  # Use the URL to the github repo.
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",  # Example license
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
)
