from setuptools import setup, find_packages

setup(
    name='tormail',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
    ],
)