import setuptools

setuptools.setup(
    name="parole",
    description="A simple password generator",
    version="0.0.2",
    author="Marius Merschformann",
    author_email="marius.merschformann@gmail.com",
    url="https://github.com/merschformann/parole",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["parole=src.generate:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
