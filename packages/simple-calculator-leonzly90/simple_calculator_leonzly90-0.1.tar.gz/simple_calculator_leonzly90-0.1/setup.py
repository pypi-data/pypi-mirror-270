import os
from setuptools import setup, find_packages

setup(
    name='simple_calculator_leonzly90',
    version='0.1',
    packages=find_packages(),
    description='A simple calculator',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/simple_calculator',  # Optional
    install_requires=[
        # Any dependencies, if you have them, e.g., 'numpy>=1.13.1',
    ],
)
