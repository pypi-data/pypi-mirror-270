import setuptools

# Read the content of the README file	
with open('README.md', encoding='utf-8') as f:	
    long_description = f.read()	

setuptools.setup(
    name="test_pkg_hmoazam",
    version="0.0.1",
    author="Hanna",
    description="Do not use",
    packages=["test_pkg_hmoazam"]
)