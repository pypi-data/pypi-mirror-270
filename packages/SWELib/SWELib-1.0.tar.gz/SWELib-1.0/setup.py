from setuptools import setup, find_packages

setup(
    name="SWELib",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'numpy==1.23.5',
        'matplotlib==3.7.1'
    ]
)
