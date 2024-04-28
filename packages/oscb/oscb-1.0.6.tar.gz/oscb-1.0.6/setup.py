from setuptools import setup, find_packages
from os import path
import sys

from io import open

here = path.abspath(path.dirname(__file__))
sys.path.insert(0, path.join(here, 'oscb'))
from version import __version__

print('version')
print(__version__)

# Get the long description from the README file
long_description = ''
readme_path = path.join(here, 'README.md')
try:
    with open(readme_path, encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    print(f"README.md not found at '{readme_path}'. No long description provided.")


setup(
    name='oscb',
    version='1.0.6',
    description='Description of your package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/oscb',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='sample setuptools development',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=[
        'torch>=1.6.0',
        'numpy>=1.16.0',
        'tqdm>=4.29.0',
        'scikit-learn>=0.20.0',
        'pandas>=0.24.0',
        'six>=1.12.0',
        'urllib3>=1.24.0',
        'outdated>=0.2.0',
        'joblib>=1.3.2'
    ],
    package_data={'oscb': ['data/*.csv']},  # Add your package data here if any
)
