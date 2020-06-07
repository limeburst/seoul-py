from setuptools import setup, find_packages

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="seoul",
    version="0.1.0",
    author="Seo Jihyeok",
    author_email="limeburst@icloud.com",
    description="Seoul public data API client library.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/limeburst/seoul-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'requests',
    ],
)
