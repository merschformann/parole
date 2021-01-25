import setuptools

# read the contents of README
from os import path

current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="parole",
    description="A simple password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.5",
    author="Marius Merschformann",
    author_email="marius.merschformann@gmail.com",
    url="https://github.com/merschformann/parole",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["parole=parole.generator:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
