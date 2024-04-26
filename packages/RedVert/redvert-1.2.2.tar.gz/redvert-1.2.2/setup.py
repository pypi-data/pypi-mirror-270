from setuptools import setup, find_packages

with open('readme.md', 'r') as file:
    description = file.read()

setup(
    name='RedVert',
    version='1.2.2',
    packages=find_packages(),
    install_requires = [
        # nothing is here
    ],
    entry_points={
        "console_scripts": [
            'redvert = redvert:Initalize',
            'redvert --version = redvert:Version',
            'redvert --learn-more = redvert:LearnMore'
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown'
)