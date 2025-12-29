from setuptools import setup, find_packages

setup(
    name="streamlang",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "antlr4-python3-runtime==4.13.1",
    ],
)