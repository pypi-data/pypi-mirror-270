from setuptools import setup, find_packages

with open('readme.md', 'r') as file:
    description = file.read()

setup(
    name='RedVert',
    version='1.2.1',
    packages=find_packages(),
    install_requires = [
        # nothing is here
    ],
    entry_points={
        "console_scripts": [
            'initredvert = redvert:Initalize',
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown'
)