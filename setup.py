from setuptools import setup, find_packages
import os


def read(file_name):
    with open(
        os.path.join(os.path.dirname(__file__), file_name), "r", encoding="utf-8"
    ) as f:
        return f.read()


setup(
    name="horizonai",
    version="0.1.18",
    packages=find_packages(),
    package_data={"": ["__init__.py"]},
    install_requires=[
        "requests",
        "click",
        "tenacity",
    ],
    entry_points={"console_scripts": ["horizonai=horizonai.cli:cli"]},
    author="Horizon Team",
    author_email="team@gethorizon.ai",
    license="MIT",
    description="Python package and command line interface to access the Horizon AI API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://www.gethorizon.ai",
    download_url="https://github.com/gethorizon-ai/horizonai-python/archive/refs/tags/v0.1.18.tar.gz",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
