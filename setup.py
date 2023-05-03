# setup.py

from setuptools import setup, find_packages

setup(
    name="horizonai",
    version="0.1.0",
    packages=find_packages(),
    package_data={"": ["__init__.py"]},
    install_requires=[
        "requests",
        "click",
    ],
    entry_points={"console_scripts": ["horizon=horizonai.cli:cli"]},
    author="Horizon Team",
    author_email="team@gethorizon.ai",
    license="MIT",
    description="Python package and command line interface to access the Horizon AI API",
    url="https://www.gethorizon.ai",
    download_url="https://github.com/gethorizon-ai/horizonai-python/archive/refs/tags/v0.1.0-alpha.tar.gz",
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
