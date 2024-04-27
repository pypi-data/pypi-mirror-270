from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="CodeBat",
    version="0.0.2.4",
    author="ShawnMerry",
    author_email="merrybili@163.com",
    description="A Python Library about Codemao API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShawnMerryCode/CodeBat",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=['requests>=2.31.0']
)
