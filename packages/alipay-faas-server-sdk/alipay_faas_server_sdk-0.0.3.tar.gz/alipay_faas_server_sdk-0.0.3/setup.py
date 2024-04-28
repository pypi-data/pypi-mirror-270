#!/usr/bin/env python3
# coding: utf-8
import re
from setuptools import setup, find_packages

NAME = "alipay-faas-server-sdk"
DESCRIPTION = "Alipay FaaS Server SDK"
PYTHON_REQUIRES = ">=3.9.0"
AUTHOR = "QiYuan"
AUTHOR_EMAIL = "lj162403@alipay.com"

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open("alipay_faas_server_sdk/__init__.py", "r") as f:
    version_line = [
        line for line in f.read().splitlines() if line.startswith("__version__")
    ][0]
ver_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
match = re.search(ver_re, version_line, re.M)
VERSION = match.group(1)

packages = find_packages(include=["alipay_faas_server_sdk", "alipay_faas_server_sdk.*"])

requires = ["requests"]
tests_require = []

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url="https://cloud.alipay.com",
    packages=packages,
    package_data={"": []},
    package_dir={"alipay_faas_server_sdk": "alipay_faas_server_sdk"},
    include_package_data=True,
    platforms=["all"],
    python_requires=PYTHON_REQUIRES,
    install_requires=requires,
    tests_require=tests_require,
    project_urls={
        "Site": "https://cloud.alipay.com",
        "Repo": "https://cloud.alipay.com",
        "Documentation": "https://opendocs.alipay.com/mini/089c99?pathHash=5a879d9a",
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
    ],
)
