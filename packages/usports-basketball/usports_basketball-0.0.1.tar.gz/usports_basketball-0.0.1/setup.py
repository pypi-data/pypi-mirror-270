from setuptools import setup, find_packages

# Constants
VERSION = '0.0.1'
DESCRIPTION = 'A Python package for USports basketball.'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='usports-basketball',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
    ],
    author='OJ Adeyemi',
    author_email='ojieadeyemi@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ojadeyemi/usports-basketball.git',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
