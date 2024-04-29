from setuptools import setup, find_packages

with open("README.md","r") as f:
    description = f.read()

setup(
    name="Cl1pAPI",
    version="0.0",
    packages=find_packages(),
    install_dependencies=[
        'requests>=2.31.0',
        'bs4>=0.0.2'
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)