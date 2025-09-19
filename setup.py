from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="Hello_and_bye",
    version="0.0.1",
    author="Matheus",
    description="Say hello and bye!",
    long_description=page_description,
    packages=find_packages(),
)