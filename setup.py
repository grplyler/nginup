from setuptools import setup, find_packages

setup(
    name="nginup",
    description="A CLI Frontend for Quick NGinx Site Configuration",
    version="0.1",
    author="Ryan Plyler <grplyler@liberty.edu>",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "nginup = nginup.cli:cli"
        ]
    },
)