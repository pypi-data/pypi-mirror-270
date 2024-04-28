from setuptools import setup, find_packages

setup(
    name='electrify-cli',
    version='0.1.0',
    author='Nularian',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'electrify = electrify.cli:cli',
        ],
    },
    description='CLI for interacting with Electrify services',
)
