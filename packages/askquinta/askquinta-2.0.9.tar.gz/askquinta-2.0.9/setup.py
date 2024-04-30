from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()
# read the contents of your README file

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='askquinta',                # Package name
    version='2.0.9',                   # Package version
    packages=find_packages(),        # Automatically find all packages and sub-packages
    #install_requires=required_packages,  # Required dependencies listed in requirements.txt
    author='Paper Data Team',        # Author name
    description='Package for daily usage of data team at Paper.id',  # Package description
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/paper-indonesia/composer',  # Package URL or project repository URL
    classifiers=[                   # Additional package classifiers (optional)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
