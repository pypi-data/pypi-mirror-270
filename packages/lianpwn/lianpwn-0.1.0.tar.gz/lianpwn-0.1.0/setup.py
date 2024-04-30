from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lianpwn",
    version="0.1.0",
    author="eastXueLian",
    author_email="eastxuelian@gmail.com",
    description="lianpwn based on pwncli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://eastxuelian.nebuu.la/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
